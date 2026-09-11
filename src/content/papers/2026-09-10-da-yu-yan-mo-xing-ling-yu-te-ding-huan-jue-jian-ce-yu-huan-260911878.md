---
title: Domain-Specific Hallucination Detection in Large Language Models
title_zh: 大语言模型领域特定幻觉检测与缓解方法
authors:
- Varun Teja Chundru
- Debasmita Biswas
affiliations:
- Purdue University Fort Wayne
arxiv_id: '2609.11878'
url: https://arxiv.org/abs/2609.11878
pdf_url: https://arxiv.org/pdf/2609.11878
published: '2026-09-10'
collected: '2026-09-11'
category: LLM
direction: 大语言模型 · 幻觉检测与缓解
tags:
- Hallucination Detection
- DeBERTa
- MC Dropout
- DPO
- Cross-domain Adaptation
one_liner: 提出结合微调DeBERTa、MC Dropout的多信号幻觉检测pipeline，可配合DPO降幻觉率55.9%
practical_value: '- 电商智能客服、导购Agent的RAG生成场景可复用该多信号检测pipeline，MC Dropout输出的不确定性高的结果直接触发二次召回/转人工，降低错误回复率

  - 生成式推荐的商品文案、卖点生成场景，仅需标注5k左右的忠实/幻觉样本即可冷启动检测器，用很低成本实现生成内容的事实校验

  - 垂直品类（3C、美妆、医药）的LLM应用做幻觉检测，优先选择对应领域预训练的底座微调，效果远好于泛域大模型直接迁移

  - 生成器幻觉优化可直接复用DPO方案，用忠实/幻觉回答构造偏好对微调，无需RLHF即可实现50%+的幻觉率相对下降'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM生成内容流畅但易出现事实性幻觉，极大限制了其在电商导购、智能客服、生成式推荐等高事实准确性要求场景的落地，现有检测方案要么仅输出点估计无法区分高/低置信度结果，要么泛域训练的模型迁移到垂直领域效果骤降，亟需兼顾准确率、可解释性和领域适配性的检测方案。
### 方法关键点
- 多信号检测pipeline：基于DeBERTa-v3微调做NLI二分类，输入拼接<query, 知识上下文, 生成回答>判断是否为幻觉
- 集成MC Dropout不确定性度量：推理时开启dropout跑20次前向，取输出概率均值作为预测结果、标准差作为不确定性信号，无需额外训练即可提升边界样本准确率
- 补充温度缩放校准概率分布，提升跨域阈值稳定性
- 配套DPO幻觉缓解方案：将忠实回答/幻觉回答作为偏好对微调生成器，用检测器做闭环效果评估
### 关键结果
在HaluEval基准测试，微调DeBERTa单模型F1=0.915、AUROC=0.977，加MC Dropout后准确率提升至93.2%，QA/摘要/对话子任务F1分别达0.97/0.96/0.82；DPO微调Qwen2.5-0.5B生成器后，幻觉率从85.5%降至37.7%，相对下降55.9%；跨域到生物医学SciFact基准，泛域模型F1仅0.52，换PubMedBERT微调后F1达0.63、AUROC=0.81；仅需25%的训练数据即可达到77%的全数据性能。
### 核心结论
垂直领域幻觉检测优先选择领域预训练底座，仅需5k左右标注样本即可冷启动可用的检测器
