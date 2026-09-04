---
title: 'ESPO: Error-Structured Prompt Optimization via Diagnose, Diversify, and Stabilize'
title_zh: ESPO：结合诊断、多样化与稳定选择的错误结构化提示优化框架
authors:
- Lihao Liu
- Peng Tang
- Kunwar Yashraj Singh
- Shabnam Ghadar
affiliations:
- AWS Agentic AI
arxiv_id: '2609.04197'
url: https://arxiv.org/abs/2609.04197
pdf_url: https://arxiv.org/pdf/2609.04197
published: '2026-09-03'
collected: '2026-09-04'
category: LLM
direction: LLM 自动化提示优化
tags:
- Prompt Optimization
- Bootstrap Selection
- Error Diagnosis
- LLM
- Evolutionary Prompt
one_liner: 解决进化式提示优化的prompt膨胀问题，在7个基准上比SOTA高3.76pp且prompt短47%
practical_value: '- 做电商/广告Agent的prompt优化时，可复用全量错误聚类诊断流程，替代随机抽样错误迭代优化，从根源避免prompt膨胀，同时降低推理token成本、提升效果

  - 生成候选prompt时可复用4种互补策略：诊断修订/规则精简/冗余规则消融/领域事实注入，比单一变异策略覆盖更多错误模式，稳定提升优化上限

  - 小验证集场景下筛选最优prompt可采用bootstrap稳定选择（推荐B=10~20次重采样），避免选到过拟合验证噪声的长prompt，大幅提升泛化性

  - 预算有限时可下调bootstrap次数到10、候选池规模到5，效果下降在1pp以内，优化速度可提升40%以上'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有进化式自动prompt优化方法（如SOTA GEPA）存在严重prompt膨胀问题：每轮迭代不断追加规则，prompt平均长度达优化后ESPO的1.87倍，准确率不升反降，额外增加推理延迟与token成本。其根源存在三个结构性缺陷：每轮仅抽样3~8个错误导致观察不完整、单一变异策略搜索多样性不足、小验证集下点估计选择不可靠易过拟合噪声。
### 方法关键点
- **Diagnose阶段**：全量收集当前prompt下的所有训练错误，用反射LLM聚类为3~7个结构化错误模式（包含根因、样例、占比），一轮即可覆盖所有系统性错误，替代GEPA需15轮才能覆盖全模式的抽样机制
- **Propose阶段**：4种互补策略生成候选prompt：①诊断修订（针对错误根因修改prompt）②规则精简（合并冗余规则、不增加长度）③冗余规则消融（删除过触发的规则）④领域事实注入（补充错误样例中的领域知识），再做2轮交叉授粉与精炼，候选池封顶10个
- **Select阶段**：采用20次bootstrap重采样验证集，选择在最多重采样中获胜的候选，平票时优先选更短的prompt，解决小验证集多测试的过拟合问题
### 关键结果
7个公开NLP基准（Tweet、MMLU、GSM8K、HotpotQA等）上，ESPO平均准确率74.67%，比SOTA GEPA高3.76pp，同时prompt短47%（1004 vs 1878字符），推理延迟更低；跨Gemma 3 12B、Mistral 14B、Qwen3 32B、Claude Haiku 4.5四个模型测试，均取得最优平均准确率，其中Qwen3 GSM8K任务从基线15%提升到91.4%，比GEPA高56pp；消融实验证实仅增加候选多样性不加bootstrap稳定选择，会导致效果下降1.2pp。
> 最值得记住的结论：多样性的候选生成必须搭配可靠的稳定选择机制，否则反而会放大过拟合噪声的影响，损害泛化性能。
