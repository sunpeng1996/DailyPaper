---
title: Stability-Compensated Threshold Calibration for Selection-Conditioned Risk
  Control in Large Language Models
title_zh: 面向大语言模型选择条件风险控制的稳定性补偿阈值校准方法
authors:
- Zhiyuan Wang
- Yuanchang Ye
- Jiahao Yuan
- Jinhao Duan
- Xiaoshuang Shi
- Weijun Xie
- Ye Wei
- Kaidi Xu
affiliations:
- City University of Hong Kong
- National University of Singapore
- East China Normal University
- University of North Carolina at Chapel Hill
- University of Electronic Science and Technology of China
arxiv_id: '2611.21384'
url: https://arxiv.org/abs/2611.21384
pdf_url: https://arxiv.org/pdf/2611.21384
published: '2026-11-16'
collected: '2026-11-17'
category: LLM
direction: 大语言模型 · 选择性预测风险控制
tags:
- Selective Prediction
- Selection Conditioned Error Rate
- Threshold Calibration
- LLM Reliability
- Finite Sample Guarantee
one_liner: 针对LEC阈值校准失效问题，提出带有限样本保证的SC-LEC框架，控制LLM选择性预测的选择后错误率
practical_value: '- 在LLM驱动的电商商品问答、智能客服、Agent决策场景中，可复用SC-LEC的校准逻辑，在控制回答错误率不超过预设阈值的前提下，最大化回答覆盖率，降低人工介入成本

  - 对于生成式推荐的候选过滤、RAG检索结果拒答、搜索query改写的风险控制场景，可借鉴锚定局部搜索+稳定性补偿的设计，避免经验阈值导致的风险超标问题

  - 工程落地时可直接复用论文的三数据拆分（选择/认证/校准）流程、KL尾部边界计算方法，快速获得1−δ高概率的风险保证，无需复杂调参'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM在问答、决策等场景下容易出现幻觉，选择性预测通过拒答高不确定性样本提升可靠性，但现有LEC方法的阈值校准依赖经验可行性判断，因损失函数非单调，无法保证选择后错误率（SCER）满足预设目标，甚至存在可复现的失效案例，亟需带严格有限样本统计保证的校准方法。
### 方法关键点
- 提出SC-LEC框架，通过全量数据参考的负线性风险补偿阈值选择的不稳定性，将部署风险分解为安全储备和稳定性间隙，当储备覆盖间隙上界时即可保证SCER≤预设阈值α
- 设计两种互补的有限样本证书：基于秩交叉的稳定性证书SC-S、基于阈值扩展结构的直接证书SC-D，后者保守性更低，相同风险约束下可获得更高的样本保留率
- 采用三独立数据拆分流程：Dsel构造阈值候选集、Dcert做锚点裕度认证、Dcal做最终阈值选择，通过KL尾部逆运算获得1−δ高概率的风险保证
### 关键实验
在CommonsenseQA、ARC-Challenge、TriviaQA三个公开QA基准上测试，对比固定锚点、原始LEC基线：α=0.2时，CommonsenseQA上SC-D比锚点基线提升6.43~10.28pct的保留率，ARC-Challenge上最高提升12.28pct，所有SC方法的实际SCER均低于预设目标；同时构造精确反例证明原始LEC的全扫描规则在i.i.d采样下确实会违反SCER目标。
### 核心结论
没有严格统计保证的经验阈值校准，哪怕在i.i.d场景下也可能出现风险超标，锚定+稳定性补偿的设计可以在可控风险下最大化业务覆盖率。
