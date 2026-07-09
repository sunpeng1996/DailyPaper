---
title: 'Seeing and Reflecting: Multimodal Memory-Enhanced Agent Collaboration for
  Recommendation'
title_zh: 多模态记忆增强多智能体协作推荐框架 MMEACR
authors:
- Hao Cong
- Huizu Lin
- Zihan Wang
- Chengkai Huang
- Quan Z. Sheng
- Lina Yao
affiliations:
- Tsinghua University
- University of Science and Technology of China
- Peking University
- The University of New South Wales
- Macquarie University
arxiv_id: '2607.07108'
url: https://arxiv.org/abs/2607.07108
pdf_url: https://arxiv.org/pdf/2607.07108
published: '2026-07-08'
collected: '2026-07-09'
category: MultiAgent
direction: 多智体多模态推荐系统优化
tags:
- Multimodal Recommendation
- LLM Agent
- Memory Mechanism
- Rank Fusion
- Multi-Agent
one_liner: 提出双轨融合的多模态记忆增强多智能体推荐框架，视觉敏感场景增益显著
practical_value: '- 多模态商品记忆初始化可直接复用：调用通用MLLM将商品主图转为结构化视觉描述，再和商品标题/属性融合生成标准化Item记忆，无需额外标注，适配服饰、家居等强视觉属性电商品类

  - 属性引导的记忆更新机制可落地：针对业务场景预定义品类属性维度（如服饰的风格、版型、材质），每次用户交互后仅基于命中属性更新用户/Item记忆，有效降低偏好漂移风险，减少记忆冗余

  - 双轨排序融合方案工程代价低：无需端到端训练，将Agent推理的可解释排序结果与多模态Embedding匹配结果通过加权RRF融合，推理速度比纯Agent方案提升6%~16%，兼顾效果和可解释性'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM驱动的Agent推荐系统普遍以文本为核心，未充分利用商品图片等视觉信号，在服饰、3C等视觉敏感场景下用户偏好刻画不足；同时记忆更新多为无约束的自由文本累积，易引入语义噪声、产生偏好漂移，长期交互后性能下降明显。
### 方法关键点
- 双轨架构设计：推理轨由User Memory Agent、Item Memory Agent维护结构化多模态记忆，支持可解释偏好推理；匹配轨保留原始交互文本、商品图片做密集多模态Embedding匹配，捕捉推理轨遗漏的细粒度信号
- 属性引导的记忆更新：预定义品类语义属性空间，每次对比正负样本交互后，从推理理由中提取关联属性，推理正确则强化对应偏好，推理错误则反思修正记忆，大幅降低噪声更新
- 加权RRF融合：将推理轨的LLM排序结果与匹配轨的余弦相似度排序结果做加权融合，输出最终排序列表，兼顾可解释性与排序精度
### 关键结果
在Amazon公开的CD、手机配件、服饰三个数据集测试，对比AgentCF、CoTAgent等主流基线：服饰场景下N@1提升45.45%、N@5提升23.33%、MRR提升27.14%；全场景推理速度比纯Agent方案AgentCF快6%~16%。
### 核心结论
Agent推荐无需完全依赖大模型端到端推理，将结构化记忆推理与轻量化多模态匹配融合，可同时实现效果提升、推理提速与可解释性保留
