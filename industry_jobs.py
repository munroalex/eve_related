#iterate through a dataframe of character tokens, only for use in testing. Use database in production.
for index, row in df.iterrows():
    security.update_token({
    'access_token': '',  # leave this empty
    'expires_in': -1,  # seconds until expiry, so we force refresh anyway
    'refresh_token': df['refresh_token'][index]
})
    #Get skill points will return what skills a character has trained to what level.
    get_skill_points = app.op['get_characters_character_id_skills'](
        character_id=df['character_id'][index]
    )
    skill_list = client.request(get_skill_points)
    # this should give a dictionary of a list of dictionaries with individual skills and total sp including unallocated
    total_sp = skill_list.data['total_sp']
    ##Calculate available manufacturing slots
    manufacturing_job_slots = 1
    manufacturing_jobs = 0
    for skill in skill_list.data['skills']:
        if skill['skill_id'] == 3387:
            if skill['active_skill_level'] != 0:
                manufacturing_job_slots = manufacturing_job_slots + skill['trained_skill_level']
        if skill['skill_id'] == 24625:
            if skill['active_skill_level'] != 0:
                manufacturing_job_slots = manufacturing_job_slots + skill['trained_skill_level']
    ##Calculate available science slots
    science_job_slots = 1
    science_jobs = 0
    for skill in skill_list.data['skills']:
        if skill['skill_id'] == 3406:
            if skill['active_skill_level'] != 0:
                science_job_slots = science_job_slots + skill['trained_skill_level']
        if skill['skill_id'] == 24624:
            if skill['active_skill_level'] != 0:
                science_job_slots = science_job_slots + skill['trained_skill_level']    
    

    #Now we grab a list of active jobs that character has
    get_industry_jobs = app.op['get_characters_character_id_industry_jobs'](
        character_id=df['character_id'][index]
    )
    jobs_list = client.request(get_industry_jobs)
    job_list_json = json.loads(jobs_list.raw)
    #if there are jobs in the list we will print out how many slots are available, else we will print out the total slots available
    if job_list_json:
        for job in job_list_json:
            if job['activity_id'] == 1:
                manufacturing_jobs += 1
            else:
                science_jobs += 1
                
        print(df['Name'][index])
        print("Manufacturing slots:")
        print(manufacturing_job_slots - manufacturing_jobs)
        print("Science slots:")
        print(science_job_slots - science_jobs)
    else:
        print(df['Name'][index])
        print("Manufacturing slots:")
        print(manufacturing_job_slots)
        print("Science slots:")
        print(science_job_slots)

    
    

