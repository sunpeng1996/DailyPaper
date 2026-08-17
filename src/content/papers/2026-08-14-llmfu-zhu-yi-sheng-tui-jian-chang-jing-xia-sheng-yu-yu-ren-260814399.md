---
title: Whose doctor does the AI recommend? An algorithm audit of reputation and demographic
  signals in large language model-assisted physician choice
title_zh: LLM辅助医生推荐场景下声誉与人口统计信号的算法审计
authors:
- Syeda Anshrah Gillani
- Mirza Samad Ahmed Baig
affiliations:
- Heidelberg University
- Fandaqah
arxiv_id: '2608.14399'
url: https://arxiv.org/abs/2608.14399
pdf_url: https://arxiv.org/pdf/2608.14399
published: '2026-08-14'
collected: '2026-08-17'
category: Eval
direction: 推荐系统公平性算法审计
tags:
- Algorithm Audit
- Recommendation Fairness
- LLM Bias
- Causal Inference
- Ranking
one_liner: 通过随机对照审计量化LLM医生推荐各特征因果影响，发现隐性人口统计偏误无法通过自解释检出
practical_value: '- 做推荐系统公平性审计时可复用本研究的「随机合成profile+特征独立扰动」的因果效应量化方法，避免真实数据的相关性混淆

  - 不要依赖LLM自生成的解释做偏误检测，本研究证明隐性偏误几乎不会出现在自解释中，需设计独立外部审计逻辑

  - 推荐列表的排序位置溢价可通过等价核心业务指标（如本研究的诊费）的方式量化，方便业务侧做排序策略ROI评估

  - 可复用本研究的可复现审计框架，对迭代后的大模型/推荐策略做固定刺激集回归测试，避免迭代引入额外偏误'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
用户愈发依赖LLM查询医生推荐，LLM作为信息中介会大规模影响医生曝光，但现有研究无法从真实世界关联数据中分离各特征对推荐结果的因果影响，也未明确人口统计信号的隐性作用。
### 方法
设计预注册随机算法审计，针对7款LLM（6款开源+GPT-4o-mini），构造3024组特征独立随机化的合成家庭医生卡片，覆盖3类患者人设、9种prompt改写、9组实验条件，共采集40068条打分响应，通过姓名标识性别与族裔，用线性概率模型估计各特征平均边际效应。
### 关键结果
声誉信号影响占主导：评分从3.9升至4.7时选择概率提升31.4pp，诊费从90美元涨至190美元时选择概率下降20.0pp；存在反常识人口统计偏误：女性、拉美/南亚/非裔姓名医生比白人姓名医生选择概率高1.3-2.9pp，等价于诊费优惠7-14美元；列表首位置等价于11美元诊费优惠；仅0.03%的偏误在LLM自解释中被提及，自报告透明度机制完全无法检出。
