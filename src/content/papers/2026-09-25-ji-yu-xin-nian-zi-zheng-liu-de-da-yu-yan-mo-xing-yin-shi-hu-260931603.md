---
title: User Model Extraction via Belief Self-Distillation
title_zh: 基于信念自蒸馏的大语言模型隐式用户模型提取方法
authors:
- Ali Holmov
- Yiran Huang
- Kirill Bykov
- Zeynep Akata
affiliations:
- Technical University of Munich
- Helmholtz Zentrum München
arxiv_id: '2609.31603'
url: https://arxiv.org/abs/2609.31603
pdf_url: https://arxiv.org/pdf/2609.31603
published: '2026-09-25'
collected: '2026-09-28'
category: LLM
direction: LLM可解释性 · 隐式用户模型提取
tags:
- LLM Interpretability
- User Modeling
- Self-Distillation
- Activation Steering
- AI Safety
one_liner: 提出信念自蒸馏框架BSD，实现LLM隐式用户信念的可读可写双向因果干预
practical_value: '- 电商/客服Agent场景可复用BSD无标注蒸馏逻辑：无需人工标注用户属性，直接以LLM自身对用户的推断信念为监督，从历史对话中蒸馏128维用户向量，替代传统用户画像用于个性化回复、意图风控

  - 生成式推荐场景可复用BSD隐式注入方案：无需在prompt中显式拼接用户属性（避免隐私泄露、prompt不稳定问题），将用户向量通过写投影矩阵注入LLM隐藏层，自然对话场景下个性化准确率比显式prompt注入高27%以上

  - 多模型部署场景可复用跨模型用户表示对齐结论：独立训练的LLM用户表示几何结构高度对齐，只需简单正交映射即可实现用户向量跨模型迁移，无需为每个模型单独训练用户建模模块'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM会从对话上下文隐式推断用户属性并自适应调整输出，但这些隐含的用户信念无法被直接观测和干预。传统探测方法仅支持读取隐藏层信息，无法验证因果效应，且依赖人工标注的外部用户属性，难以对齐LLM自身的真实信念，限制了个性化、安全风控等场景的落地。

### 方法关键点
- 设计信念自蒸馏（BSD）读写统一框架，冻结两份相同LLM分别作为教师、学生，仅训练低秩读写投影矩阵：读矩阵A从教师隐藏层压缩出128维用户向量，写矩阵B将用户向量正交注入学生隐藏层
- 以LLM自身对用户属性的多选项问答输出为蒸馏监督，无需外部标注，训练目标最小化师生输出的KL散度
- 支持双向能力：读取侧通过线性探针解码用户属性，写入侧通过对比激活加法实现用户信念的因果干预

### 关键结果
- 实验覆盖Llama-3.1-8B、Qwen3-8B、OLMo-3-7B三个模型，训练数据为27k WildChat真实对话+31k WildJailbreak对抗对话
- 128维用户向量保留原始隐藏层96%以上的可解码信息，线性探针F1差距<4%；干预效果比直接操作原始隐藏层高13%~57%，Llama-3.1上信念翻转率达78%
- 用户意图向量预测LLM拒绝回答的AUC达0.94，干预用户意图可将有害请求的拒绝率从98%降至62%；不同LLM的用户表示几何结构高度对齐，跨模型信念迁移成功率达53%~54%

> 最值得记住的结论：LLM的拒绝决策不仅取决于请求本身，还取决于它对用户意图的隐式推断，隐式用户模型是可被读取和因果编辑的内部状态
