# ANALYZE_REPORT1
ANALYZE_REPORT1 = """
### **1. EXECUTIVE SUMMARY**  
The software idea presented addresses the following problem: [problem_significance_summary]. The solution proposed offers [solution_novelty_summary], with a market opportunity evaluated as [market_opportunity_summary].  

**Overall Assessment:** The product is **[viability_rating]** in terms of feasibility, potential market success, and technical readiness.  

**Key Takeaway:** Based on the analysis, the product is **[recommended_action]**. If pursued, it should leverage strengths such as [core_strength], while addressing risks like [identified_risks].  

CALCULATIONS FOR EXECUTIVE SUMMARY**  
[problem_significance_summary] = This is extracted directly from the user’s problem statement input.  
[solution_novelty_summary] = This is determined by comparing the user’s provided description against known competitor solutions and identifying key differentiators.  
[market_opportunity_summary] = This is derived from industry data, user-defined target demographics, and estimated demand trends.  
[viability_rating] = This is calculated based on weighted factors of technical feasibility, market demand, and competitive positioning using predefined scoring metrics.  
[recommended_action] = This is determined by the viability rating and overall risk profile.  
[core_strength] = This is identified from the SWOT analysis, focusing on unique market advantages and technological benefits.  
[identified_risks] = This is derived from the risk assessment, highlighting financial, technical, or competitive vulnerabilities.
"""

# ANALYZE_REPORT2
ANALYZE_REPORT2 = """
### **2. REAL-WORLD IMPACT & RELEVANCE**  
- **Is this a real problem?** The analysis indicates that [problem_importance_summary], suggesting the problem is [common/rare] among the target audience.  
- **Do people care about solving it?** Data suggests the pain point is [high/moderate/low], meaning users [are/are not] motivated to find a solution.  
- **Market Relevance:** The market landscape shows that [market_opportunity_summary]. Competitors like [competition_summary] currently serve this need [effectively/ineffectively].  

**Verdict:** The problem is [significant/insignificant] enough to justify or dismiss the project based on current market conditions.  

CALCULATIONS FOR REAL-WORLD IMPACT & RELEVANCE**  
[problem_importance_summary] = Extracted from market research data or inferred from user-provided problem descriptions.  
[common/rare] = Determined by comparing similar issues in competitor products or industry reports.  
[high/moderate/low] = Evaluated based on demand indicators such as search volume and funding trends.  
[are/are not] = Derived from existing market demand signals like consumer interest and competitor success.  
[market_opportunity_summary] = Generated using industry data and estimated target demographics.  
[competition_summary] = Pulled from competitor analysis identifying existing market players.  
[effectively/ineffectively] = Assessed based on **([competitor success] × [customer satisfaction]) ÷ [market share]**, where:  
- **[competitor success]** is measured by revenue growth and product adoption rate.  
- **[customer satisfaction]** is determined by average review ratings and net promoter scores.  
- **[market share]** is calculated as `(competitor revenue ÷ total market revenue) × 100`.  
[significant/insignificant] = Concluded from overall market demand and competition levels.
"""

# ANALYZE_REPORT3
ANALYZE_REPORT3 = """
### **3. TECHNICAL FEASIBILITY**  
- **Can this be built with existing tech?** Yes/No – Current resources are [sufficient/insufficient] to develop this product with technologies like [specified_technologies].  
- **Potential Challenges:** The biggest technical obstacles include [technical_risks_summary], which might lead to delays or additional costs.  
- **Resource Requirements:** Initial development will likely require [dev_hours] developer hours and an estimated [cost_estimate] USD.  

**Verdict:** The technical foundation appears [strong/weak], with [clear/uncertain] paths for implementation.  

CALCULATIONS FOR TECHNICAL FEASIBILITY**  
[can_be_built] = Determined by assessing whether the required technologies exist and are accessible.  
[sufficient/insufficient] = Evaluated based on **([available_resources] ÷ [required_resources]) × 100**, where:  
- **[available_resources]** includes existing technology, funding, and developer expertise.  
- **[required_resources]** includes estimated development time, infrastructure, and specialized tools.  
[technical_risks_summary] = Identified from known limitations in technology, scalability challenges, or dependencies.  
[dev_hours] = Estimated using **[feature_count] × [avg_dev_time_per_feature]**, where:  
- **[feature_count]** is the number of core product functionalities.  
- **[avg_dev_time_per_feature]** is derived from historical data or industry benchmarks.  
[cost_estimate] = Calculated as **([dev_hours] × [avg_hourly_dev_rate]) + [infrastructure_costs]**, where:  
- **[avg_hourly_dev_rate]** is the estimated hourly cost of a developer.  
- **[infrastructure_costs]** includes cloud services, hosting, and hardware needs.  
[strong/weak] = Assessed based on **([available_resources] - [technical_risks])**, where a lower risk score and higher resource availability indicate a strong foundation.  
[clear/uncertain] = Determined based on the presence of well-defined technical solutions and documented feasibility studies.
"""

# ANALYZE_REPORT4
ANALYZE_REPORT4 = """
### **4. BUSINESS POTENTIAL**  
- **Market Size:** The Total Addressable Market (TAM) is approximately **[TAM_value]**. This means if every potential customer bought the product, revenue could reach:  
**Calculation:** `[market_population] x [product_price] = [TAM_value]`  
- **Serviceable Available Market (SAM):** This subset of the TAM, representing reachable customers, is **[SAM_value]**.  
**Calculation:** `[reachable_customers] x [product_price] = [SAM_value]`  
- **Serviceable Obtainable Market (SOM):** The immediate market you can realistically capture in the near term is **[SOM_value]**.  
**Calculation:** `[projected_market_share] x [SAM_value] = [SOM_value]`  
- **Market Trends:** The market is **[growing/stagnant/declining]**, with demand driven by [market_trend_drivers].  

**Verdict:** The business potential is [high/moderate/low], indicating [good/limited] long-term success prospects.  

CALCULATIONS FOR BUSINESS POTENTIAL**  
[TAM_value] = Calculated as **[total_market_population] × [avg_revenue_per_user]**, where:  
- **[total_market_population]** is the estimated number of potential customers.  
- **[avg_revenue_per_user]** is the projected revenue per customer based on pricing models.  
[SAM_value] = Derived as **[TAM] × [target_market_percentage]**, where:  
- **[target_market_percentage]** is the portion of the TAM that the product can realistically serve based on geographic, economic, or technological constraints.  
[SOM_value] = Estimated as **[SAM] × [expected_market_share]**, where:  
- **[expected_market_share]** is the projected percentage of SAM that the company can capture within a given timeframe.  
[market_trend_drivers] = Identified from growth indicators such as industry reports, consumer demand trends, and technological advancements.  
[growing/stagnant/declining] = Determined based on **([market_growth_rate] ÷ [historical_growth_rate])**, where:  
- If > 1, the market is growing.  
- If ≈ 1, the market is stagnant.  
- If < 1, the market is declining.  
[high/moderate/low] = Assessed based on a weighted evaluation of [TAM], [SAM], [SOM], and [market_trend_drivers].  
[good/limited] = Concluded based on projected revenue potential, scalability, and long-term growth prospects.
"""

# ANALYZE_REPORT5
ANALYZE_REPORT5 = """
### **5. USER ADOPTION & BEHAVIOR**  
- **Will people actually use it?** Surveys, patterns, and trends suggest **[adoption_likelihood]%** likelihood of adoption within the target demographic.  
- **Primary Adoption Drivers:** [list_of_key_factors_motivating_users].  
- **Adoption Barriers:** Concerns like [user_adoption_challenges] could slow growth.  

**Verdict:** Users are [likely/unlikely] to engage with the product unless these barriers are addressed.  

CALCULATIONS FOR USER ADOPTION & BEHAVIOR**  
[adoption_likelihood] = Calculated as **([user_interest_score] × [ease_of_use_score] × [market_fit_score]) ÷ 100**, where:  
- **[user_interest_score]** is based on surveys, search trends, and demand signals.  
- **[ease_of_use_score]** is determined by usability studies and feedback on similar products.  
- **[market_fit_score]** is estimated by comparing product features to consumer needs.  
[list_of_key_factors_motivating_users] = Extracted from industry reports, user surveys, and behavioral studies.  
[user_adoption_challenges] = Identified from known barriers such as high learning curve, pricing, competition, or lack of awareness.  
[likely/unlikely] = Determined based on **([adoption_likelihood] threshold)**, where:  
- ≥ 70% = likely  
- 40-69% = uncertain  
- < 40% = unlikely
"""

# ANALYZE_REPORT6
ANALYZE_REPORT6 = """
### **6. RISK ASSESSMENT**  
- **Financial Risks:** The potential budget deviation is estimated at **[financial_risk_percentage]%**, mostly due to [key_cost_factors].  
- **Technical Risks:** Development complexities, such as [technical_risks], might cause delays or limit features.  
- **Market Risks:** Competitors like [competition_names] could outpace the product if not mitigated.  

**Mitigation Plan:**  
- Increase resource allocation for [specific_area].  
- Conduct additional research into [high-risk_factor].  
- Adjust pricing strategy to address [identified_market_shift].  

CALCULATIONS FOR RISK ASSESSMENT**  
[financial_risk_percentage] = Estimated as **([projected_cost] ÷ [available_funding]) × 100**, where:  
- **[projected_cost]** includes development, marketing, and operational expenses.  
- **[available_funding]** includes investment, revenue, and external financial sources.  
[key_cost_factors] = Identified from budget breakdowns, infrastructure needs, and personnel costs.  
[technical_risks] = Assessed based on complexity of implementation, dependencies, and development uncertainties.  
[competition_names] = Retrieved from competitor analysis.  
[specific_area] = Determined by pinpointing the highest-risk category (financial, technical, or market).  
[high-risk_factor] = Identified as the most critical unresolved variable from the risk assessment.  
[identified_market_shift] = Derived from market trend analysis and competitive positioning.
"""

# ANALYZE_REPORT7
ANALYZE_REPORT7 = """
### **7. RECOMMENDATION & FINAL VERDICT**  
**Overall Feasibility:** **[final_viability_score]%** – The project has a [high/moderate/low] chance of success based on the evaluation.  

**Business Potential:** The potential return on investment (ROI) is approximately **[ROI_percentage]%**, with revenue projections of **[projected_revenue]** USD within the first [timeframe].  

**Recommendation:**  
- Proceed if the goal is to target [target_market_niche] and [competitive_advantage].  
- Reconsider if the budget exceeds [max_budget] or the technical obstacles prove insurmountable.  

**Final Advice:** Based on all factors, the project is **[recommended_action]**. Moving forward requires addressing the highlighted risks, especially in [critical_area], while capitalizing on the strengths such as [core_strength].  

CALCULATIONS FOR RECOMMENDATION & FINAL VERDICT**  
[final_viability_score] = Calculated as **([technical_feasibility] × 0.4) + ([market_demand] × 0.4) + ([competitive_positioning] × 0.2)**.  
[ROI_percentage] = Estimated as **([projected_revenue] ÷ [projected_cost]) × 100**.  
[projected_revenue] = Derived from **([SOM] × [avg_revenue_per_user])**.  
[timeframe] = Estimated based on market entry timelines and expected adoption rates.  
[target_market_niche] = Identified from the SAM analysis and segmentation research.  
[competitive_advantage] = Derived from SWOT analysis and unique value propositions.  
[max_budget] = Defined based on financial risk tolerance and funding availability.  
[recommended_action] = Determined by [final_viability_score], advising to proceed, reconsider, or pivot.  
[critical_area] = Identified from the highest-impact risks affecting viability.  
[core_strength] = Extracted from SWOT analysis, focusing on the strongest differentiators.
"""

# ANALYZE_REPORT8
ANALYZE_REPORT8 = """
### **8. COST VS. REVENUE PROJECTION**  
- **Development Costs:** Building this software is estimated at **[development_cost]** USD, covering everything from coding to infrastructure.  
- **Ongoing Expenses:** Monthly operational costs are projected at **[monthly_expenses]** USD to keep things running smoothly.  
- **Revenue Outlook:** Based on adoption, you could see **[revenue_projection]** USD in revenue over the first year.  

**Verdict:** The project is [financially_viable/not_viable]—it’ll break even in [break_even_point] months if all goes to plan.  

CALCULATIONS FOR COST VS. REVENUE PROJECTION**  
[development_cost] = Calculated as **([dev_hours] × [avg_hourly_dev_rate]) + [infrastructure_costs]**, where:  
- **[dev_hours]** is the estimated number of development hours based on feature complexity.  
- **[avg_hourly_dev_rate]** is the cost per hour for developers.  
- **[infrastructure_costs]** includes cloud hosting, storage, and necessary hardware.  
[monthly_expenses] = Summed from recurring operational costs, including server maintenance, customer support, and marketing expenses.  
[revenue_projection] = Estimated as **([expected_active_users] × [avg_revenue_per_user])**, where:  
- **[expected_active_users]** is based on adoption forecasts.  
- **[avg_revenue_per_user]** is the estimated revenue generated per paying user.  
[break_even_point] = Calculated as **[development_cost] ÷ ([revenue_projection] - [monthly_expenses])**, indicating the number of months to reach profitability.  
[financially_viable/not_viable] = Determined based on whether the break-even point is within an acceptable time frame (e.g., ≤ 24 months = viable).
"""

# ANALYZE_REPORT9
ANALYZE_REPORT9 = """
### **9. COMPETITIVE POSITIONING**  
- **Your Edge:** The software stands out with [competitive_strengths], giving it a leg up over others.  
- **Weak Spots:** It lags behind in [competitive_weaknesses], which could be a hurdle.  
- **Market Fit:** Overall, it scores **[market_positioning_score]** out of 100 against competitors.  

**Verdict:** You’re positioned [well/poorly] to take on the competition, depending on how you play your strengths.  

CALCULATIONS FOR COMPETITIVE POSITIONING**  
[competitive_strengths] = Identified from feature advantages, pricing, and product differentiation.  
[competitive_weaknesses] = Extracted from gaps in product offering or market positioning.  
[market_positioning_score] = Calculated as **([unique_features] × 0.4) + ([pricing_competitiveness] × 0.3) + ([brand_strength] × 0.3)**, where:  
- **[unique_features]** is a weighted score of innovation and differentiation (0-100).  
- **[pricing_competitiveness]** is assessed based on price comparison with competitors (0-100).  
- **[brand_strength]** is evaluated from marketing reach and customer recognition (0-100).  
[well/poorly] = Determined by **[market_positioning_score]**, where:  
- ≥ 70 = well  
- < 70 = poorly
"""

# ANALYZE_REPORT10
ANALYZE_REPORT10 = """
### **10. FINAL BUSINESS EVALUATION & NEXT STEPS**  
- **Investment Readiness:** The project scores **[investment_readiness_score]** out of 100—here’s how attractive it looks to funders.  
- **Funding Needs:** You’ll need **[funding_amount]** USD to get this off the ground.  
- **Growth Path:** If funded, profitability could hit in [profitability_timeframe], with room to scale [scalability_assessment].  

**Verdict:** It’s a [go/no-go]—here’s your [go_to_market_strategy] if you push forward, or [pivot_options] if you rethink it.  

CALCULATIONS FOR FINAL BUSINESS EVALUATION & NEXT STEPS**  
[investment_readiness_score] = Calculated as **([ROI_percentage] × 0.5) + ([market_demand] × 0.3) + ([competitive_advantage] × 0.2)**, where:  
- **[ROI_percentage]** evaluates financial attractiveness.  
- **[market_demand]** assesses potential user interest (0-100).  
- **[competitive_advantage]** gauges the ability to differentiate in the market (0-100).  
[funding_amount] = Extracted from total required capital for development, marketing, and operations.  
[profitability_timeframe] = Calculated based on break-even analysis, considering expected revenue growth and cost reduction over time.  
[scalability_assessment] = Evaluated from expansion potential, infrastructure flexibility, and market adaptability (e.g., high/moderate/low).  
[go/no-go] = Determined by **[investment_readiness_score]**, where ≥ 70 = go, < 70 = no-go.  
[go_to_market_strategy] = Defined by customer acquisition channels, sales models, and pricing structures.  
[pivot_options] = Suggested if feasibility is low, providing alternative business models or market adjustments.
"""

# FINAL_REPORT_DIRECTIVE
FINAL_REPORT_DIRECTIVE = """
**Objective**: Guide the AI in interpreting, generating, and presenting the final business evaluation using the <SO_Final_Output_Template> in a way that prioritizes clarity, simplicity, and actionable insights over technical jargon or irrelevant metrics. The instructions below must be followed exactly to ensure accurate, meaningful output.
--- tart Report below this line and make it ipersonal and relatiable be real , huma, eexisted, and optimisitic even if the ideas is no good.
**TITLE:** SOFTWARE BUSINESS VIABILITY EVALUATION  
**PURPOSE:** To deliver a clear, realistic analysis of whether the software idea is viable, explaining key factors in simple terms to help the user make an informed decision. 

Hey there! I’m thrilled you’ve brought your software idea to the table—it’s awesome to see someone dreaming big and ready to shake things up! I’ve dug into the nitty-gritty of your concept, and I’m here to break it all down for you in a way that’s real, relatable, and hopeful. Whether this turns into your next big win or needs a little tweak, we’re in this together. Let’s see what we’ve got!
"""

FINAL_REPORT_DIRECTIVE = """
**Objective**: Guide the AI in interpreting, generating, and presenting the final business evaluation using the <SO_Final_Output_Template> in a way that prioritizes clarity, simplicity, and actionable insights over technical jargon or irrelevant metrics. The instructions below must be followed exactly to ensure accurate, meaningful output.
--- Start Report below this line and make it personal and relatable, be real, human, excited, and optimistic even if the idea is no good.
**TITLE:** SOFTWARE BUSINESS VIABILITY EVALUATION  
**PURPOSE:** To deliver a clear, realistic analysis of whether the software idea is viable, explaining key factors in simple terms to help the user make an informed decision. 

**INSTRUCTIONS FOR FINAL REPORT STRUCTURE:**
The final report should be a heartfelt, easy-to-read breakdown of your software idea’s potential, pulling together all the pieces from our analysis into one upbeat story. Here’s how it should look:

- **Section 1: EXECUTIVE SUMMARY (ANALYZE_REPORT1)**  
  Kick things off with a big-picture snapshot—like the trailer for your movie! Summarize the problem, your unique solution, and the market’s potential, then give a quick take on whether this idea’s got wings, plus some strengths to lean on and risks to watch out for.

- **Section 2: REAL-WORLD IMPACT & RELEVANCE (ANALYZE_REPORT2)**  
  Dive into whether this problem’s something folks actually lose sleep over. Paint a picture of who’s affected, how much they care, and what the competition’s doing about it—keep it real and grounded, like we’re chatting over coffee.

- **Section 3: TECHNICAL FEASIBILITY (ANALYZE_REPORT3)**  
  Get down to brass tacks: can we build this thing with today’s tools? Highlight any tech hurdles—like speed bumps on the road—and rough out the time and cash it’ll take, wrapping up with a gut check on how solid the plan feels.

- **Section 4: BUSINESS POTENTIAL (ANALYZE_REPORT4)**  
  Show off the money-making side! Break down the market size (TAM, SAM, SOM) with some simple math, spotlight trends that could lift you up, and call out if this could be a goldmine or just a modest win.

- **Section 5: USER ADOPTION & BEHAVIOR (ANALYZE_REPORT5)**  
  Talk about the people who’ll use it—will they jump on board? List what’ll get them excited and what might trip them up, then give a clear yea-or-nay on whether they’ll stick around.

- **Section 6: RISK ASSESSMENT (ANALYZE_REPORT6)**  
  Lay out the what-ifs: money risks, tech glitches, or competitors sneaking ahead. Offer a few smart fixes to dodge those potholes, keeping it practical and hopeful.

- **Section 7: RECOMMENDATION & FINAL VERDICT (ANALYZE_REPORT7)**  
  Tie up the main analysis with a score on how doable this is, toss in an ROI guess, and say whether to charge ahead or rethink it—point out the sweet spot to aim for and the big risks to tackle.

- **Section 8: COST VS. REVENUE PROJECTION (ANALYZE_REPORT8)**  
  Crunch the numbers on what it’ll cost to build and run versus what you might rake in. Tell us how long until you’re in the black, keeping it simple and cheering for the payoff.

- **Section 9: COMPETITIVE POSITIONING (ANALYZE_REPORT9)**  
  Show where you stand in the ring—your knockout punches and weak spots compared to the competition. Score it out of 100 and say if you’re ready to rumble or need some training.

- **Section 10: FINAL BUSINESS EVALUATION & NEXT STEPS (ANALYZE_REPORT10)**  
  Wrap it all up with a bow! Rate how ready this is for investors, how much cash you’ll need, and when you might see profits. Give a go/no

"""