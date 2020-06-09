# Outline:

(Blurb from the Graph Theory Course by UCSD)

- We'll develop an algorithm which finds stable matchings in bipartite graphs. This algorithm solves the problem of matching students with schools, doctors with hospitals, and organ donors with patients. By the end of this week, we'll implement an algorithm which won the Nobel Prize in Economics!
- The algorithm in question is the renowned Gale-Shapley Algorithm that seeks to find stable matchings in bipartite graphs.
- A bipartite graph is one where the objects can be partitioned into 2 sets that only interact with each other and not amongst their own set - for our example, the 2 sets are men and women and their interaction is in the form of a marriage. As the algorithm only allows for a bipartite graph, only heterosexual marriages are considered and this is in **no way indicative of my socio-political orientation.**
- The idea of marriage is used as it makes variable names rather easy since we can consider men and women and their preferences.
- A stable match, which this algorithm strives to achieve, is a situation in which no pair of people prefer each other over their partners.
- A detailed description of how the algorithm works is below and a video to further understand the algorithm and idea of stable matches is this one by [Numberphile](https://www.youtube.com/watch?v=Qcv1IqHWAzg&t=13s).

# Purpose:

- Implementing this algorithm was the final project in my Graph Theory course as part of the Discrete Math Specialisation by UCSD and the National Research University Higher School of Economics.
- The course was extremely engaging and taught me how to utilise graphs in computer science and find optimal solutions to problems through algorithms such as this one and the Ford-Fulkerson Theorem.
- I thoroughly enjoyed the project as it introduced me to a practical implementation of a theoretical idea - an implementation which garnered a Nobel Prize no less.

# Description:

- The algorithm works through the idea of non-deterministic partial matches at each iteration:
    - Each man proposes to the woman at the top of his list regardless of whether she is married or not and then she chooses the proposal from the man that is at the top of her list.
    - If she is not married, she just accepts any proposal.
    - If she is married, then she sees whether she prefers her current husband or the man that has just proposed to her.
    - The unmarried men then propose to the next highest person on their list.
    - This process continues until each person has been paired up.
- The task of the project was to create a function that took the number of men and women; n, the preferences of the men, menPreferences and the preferences of women, womenPreferences.
- The men and women were named from 0 to n-1 to make the program easier as I could just use lists instead of dictionaries.
- Ultimately, I had to return a list where the index position refers to the man and the value at the index position was the women that he was married to.
- The preferences were a 2-d array where each index position referred to the man and the list at any index position contained all n women ranked in descending order according to his preference of them.
- The same format was also followed for the women.
- For convenience I also stored:

    ```python
    unmarriedMen = [i for i in range(n)] #men that are not married
    manSpouse = [None for i in range(n)] #wife of each man -> to be returned
    womanSpouse = [None for i in range(n)] #husband of each woman
    nextManChoice = [0 for i in range(n)] #no. of proposals made by each man
    ```

- The working crux of a program was a while loop that ran while there were men who were unmarried:

    ```python
    while unmarriedMen:
            man = unmarriedMen[0]
            his_preferences = menPreferences[man]
            woman = his_preferences[nextManChoice[man]]
            nextManChoice[man] += 1
            her_preferences = womenPreferences[woman]
            husb = womanSpouse[woman]
            if husb != None:
                if her_preferences.index(husb) > her_preferences.index(man):
                    womanSpouse[woman], manSpouse[man] = man, woman
                    unmarriedMen.append(husb)
                    unmarriedMen.remove(man)
            else:
                womanSpouse[woman], manSpouse[man] = man, woman
                unmarriedMen.remove(man)
    ```

    - Here the current man is arbitrarily chosen and his preferences are logged. The woman he will propose to next is logged and so are her preferences. His proposal is logged and no. of proposals is amended.
    - If she is married, then her preference is accounted for and the respective man is made her preference and the other is added to the unmarried list and the list of manSpouse is reflected.
    - If she isn't married then she is married off to the man tentatively until another person proposes to her who she prefers (unless of course by some luck she is proposed to by the person at the top of her list - thus in this scenario, it only ever gets better for the women.)
    - P.S the if husb != None is used instead of the more pythonic if not husb as there is a man named 0 and that would give false, causing a bug.
