---
title: Training-Free Task Vectors for LLM Behavioral Control
title_zh: 无需训练的任务向量实现大语言模型行为控制
authors:
- Gabriel J. Perin
- Lucas Boscaini
- André Araujo
- Nina S. T. Hirata
affiliations:
- University of São Paulo
- Google
- Google DeepMind
arxiv_id: '2609.09054'
url: https://arxiv.org/abs/2609.09054
pdf_url: https://arxiv.org/pdf/2609.09054
published: '2026-09-08'
collected: '2026-09-09'
category: LLM
direction: LLM后训练 · 无训练行为编辑
tags:
- Task Vector
- Model Editing
- Activation Steering
- Training-Free
- LLM Alignment
one_liner: 无需微调仅用前向统计量映射激活转向向量为权重空间任务向量，实现LLM可组合行为编辑
practical_value: '- 垂直场景Agent行为对齐：比如电商客服、营销Agent需要调整输出风格/合规性时，仅需准备几十组对比Prompt即可生成TFTV，无需微调，大幅降低对齐成本

  - 生成式推荐文案控制：需要控制推荐文案的风格（活泼/专业）、抑制幻觉/过度营销内容时，用TFTV做权重编辑比推理时注入转向向量效果更强，且不增加推理开销

  - 多约束场景快速组合：如需同时满足「文案合规」「符合用户偏好」「突出商品卖点」多个要求，直接叠加对应TFTV即可，无需重新训练或调参'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
传统任务向量依赖先微调得到目标模型再计算权重差，每个行为控制需求都要单独微调，成本极高；而推理时激活转向是临时干预，会破坏标准推理管线兼容性，且效果有限，无法满足落地场景快速、低成本调整LLM行为的需求。
### 方法关键点
- 先通过对比Prompt集（分别诱导/抑制目标行为）生成响应，经LLM judge过滤不符合要求的样本后，计算正负样本的激活均值差得到激活转向向量
- 对目标模块（如注意力输出投影层）权重做SVD，结合模块的期望输入向量，将激活转向向量映射为秩一权重更新（即TFTV），更新规模与原权重范数自动匹配，无需跨层调参
- 天然满足算术性质：加TFTV放大目标行为、减TFTV抑制目标行为、多个TFTV直接相加即可组合多个行为控制需求
### 关键结果
在Llama 3.1 8B、Qwen 2.5 7B等4个主流指令微调模型上测试，对比激活转向、Steer2Edit等无训练基线，以及需要微调的Task Vector、CWS基线：
- 放大目标行为时，5/6个场景下TFTV的 trait 得分比最优无训练基线高5.57~53.38分，MMLU仅下降0.15分以内，通用能力保留远优于其他无训练方法
- 抑制目标行为时，比激活转向基线的trait得分低7.74~77.28分，GSM8K得分下降不到1分
- 多行为组合编辑时，效果优于单个编辑叠加，MMLU下降最多0.11分

**最值得记住的一句话**：无需任何微调，仅用几十组对比Prompt的前向统计量就能得到效果接近微调任务向量、通用能力保留更好的可组合权重编辑向量，是LLM落地场景快速做行为对齐的极低门槛方案。
