for index, row in df.iterrows():
    security.update_token({
    'access_token': '',  # leave this empty
    'expires_in': -1,  # seconds until expiry, so we force refresh anyway
    'refresh_token': df['refresh_token'][index]
})
    get_skill_points = app.op['get_characters_character_id_skills'](
        character_id=df['character_id'][index]
    )
    skill_list = client.request(get_skill_points)
    #print(skill_list.data)
    # this should give a dictionary of a list of dictionaries with individual skills and total sp including unallocated
    total_sp = skill_list.data['total_sp']
    ##Manufacturing
    job_slots = 1
    manufacturing_jobs = 0
    for skill in skill_list.data['skills']:
        if skill['skill_id'] == 3387:
            if skill['active_skill_level'] != 0:
                job_slots = job_slots + skill['trained_skill_level']
        if skill['skill_id'] == 24625:
            if skill['active_skill_level'] != 0:
                job_slots = job_slots + skill['trained_skill_level']
    print(df['Name'][index])
    

    #/characters/{character_id}/industry/jobs/
    get_industry_jobs = app.op['get_characters_character_id_industry_jobs'](
        character_id=df['character_id'][index]
    )
    jobs_list = client.request(get_industry_jobs)
    job_list_json = json.loads(jobs_list.raw)
    print("Manufacturing slots:")
    if job_list_json:
        for job in job_list_json:
            if job['activity_id'] == 1:
                manufacturing_jobs += 1
        print(job_slots - manufacturing_jobs)
    else:
        print(job_slots)
    ##Science
    job_slots = 1
    science_jobs = 0
    for skill in skill_list.data['skills']:
        if skill['skill_id'] == 3406:
            if skill['active_skill_level'] != 0:
                job_slots = job_slots + skill['trained_skill_level']
        if skill['skill_id'] == 24624:
            if skill['active_skill_level'] != 0:
                job_slots = job_slots + skill['trained_skill_level']
    
    

    #/characters/{character_id}/industry/jobs/
    get_industry_jobs = app.op['get_characters_character_id_industry_jobs'](
        character_id=df['character_id'][index]
    )
    jobs_list = client.request(get_industry_jobs)
    job_list_json = json.loads(jobs_list.raw)
    print("Science slots:")
    if job_list_json:
        for job in job_list_json:
            if job['activity_id'] != 1:
                science_jobs +=1
        print(job_slots - science_jobs)
    else:
        print(job_slots) 
