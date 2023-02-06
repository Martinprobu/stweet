import stweet as st
import time


def try_search():
    search_tweets_task = st.SearchTweetsTask(all_words='#covid19')
    output_jl_tweets = st.JsonLineFileRawOutput('output_raw_search_tweets.jl')
    output_jl_users = st.JsonLineFileRawOutput('output_raw_search_users.jl')
    output_print = st.PrintRawOutput()
    st.TweetSearchRunner(search_tweets_task=search_tweets_task,
                         tweet_raw_data_outputs=[output_print, output_jl_tweets],
                         user_raw_data_outputs=[output_print, output_jl_users]).run()


def try_user_scrap():
    user_task = st.GetUsersTask(['iga_swiatek'])
    output_json = st.JsonLineFileRawOutput('output_raw_user.jl')
    output_print = st.PrintRawOutput()
    st.GetUsersRunner(get_user_task=user_task, raw_data_outputs=[output_print, output_json]).run()


def try_tweet_by_id_scrap():
    id_task = st.TweetsByIdTask('1447348840164564994')
    # id_task = st.TweetsByIdTask('1447349387949129729')
    
    output_json = st.JsonLineFileRawOutput('output_raw_id.jl')
    
    output_print = st.PrintRawOutput()
    st.TweetsByIdRunner(tweets_by_id_task=id_task,
                        raw_data_outputs=[output_print]).run()


if __name__ == '__main__':
    start_time = int(time.time() - 120)
    print("start_time : %s, datetime : %s, gain : %s============================ start_time "%(start_time, time.ctime(start_time), 'gain'))
    # try_search()
    # try_user_scrap()

    try_tweet_by_id_scrap()
    end_time = int(time.time() - 120)
    print("end_time : %s, datetime : %s, gain : %s============================ end_time "%(end_time, time.ctime(end_time), end_time - start_time))
