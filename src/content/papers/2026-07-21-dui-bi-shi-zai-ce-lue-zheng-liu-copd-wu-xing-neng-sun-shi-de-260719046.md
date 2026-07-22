---
title: Contrastive On-Policy Distillation
title_zh: 对比式在策略蒸馏COPD：无性能损失的大模型推理压缩方法
authors:
- Jiacheng Ruan
- Jun Tang
- Wenzhen Yuan
- Ting Liu
- Shuai Bai
- Dayiheng Liu
- Zhibo Yang
- Yuzhuo Fu
affiliations:
- Shanghai Jiao Tong University
- Alibaba Group
arxiv_id: '2607.19046'
url: https://arxiv.org/abs/2607.19046
pdf_url: https://arxiv.org/pdf/2607.19046
published: '2026-07-21'
collected: '2026-07-22'
category: Training
direction: 大模型蒸馏 · 推理效率优化
tags:
- On-Policy Distillation
- Contrastive Learning
- Reasoning Compression
- Knowledge Distillation
- PPO
one_liner: 基于轻/重推理模式的对比token级优势信号，实现无性能损失的LLM推理长度压缩
practical_value: '- 做电商导购Agent、多轮对话推荐推理优化时，可复用COPD的轻/重思考对比范式，无需硬加长度惩罚即可压缩思考链长度，降低推理时延，适配高并发实时响应场景

  - 业务场景中小模型蒸馏可直接用COPSD自蒸馏变体，无需额外大教师模型，仅用模型自身快照做对比信号，就能在保性能前提下压缩推理输出长度，降低部署成本

  - 做LLM-based商品文案、营销话术生成时，可将轻/重思考prompt替换为不同风格/长度约束，通过对比优势信号引导模型输出符合业务要求的短文案，无需人工标注偏好对

  - 训练侧可复用对比优势+PPO的范式，相比传统OPD训练GPU耗时降低50%以上，节省大模型微调的算力成本'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有On-policy Distillation（OPD）仅基于单一教师分布提供token级监督，无法区分生成步骤是有效推理还是冗余展开；传统推理压缩方法依赖人工长度惩罚、标注偏好对，容易损失模型性能，难以自适应去除冗余推理步骤，大模型推理时延高的问题在高并发电商导购、推荐Agent等场景尤为突出。
### 方法关键点
- 引入轻思考（LT）、重思考（HT）两类前置指令，对学生模型on-policy生成的同一token，分别用冻结教师计算两类上下文下的对数概率
- 定义token级对比优势为LT概率减HT概率，正优势表示该token适配高效推理，负优势表示属于冗余步骤，裁剪后作为PPO更新的奖励信号
- 支持无外部教师的自蒸馏变体COPSD，用训练中模型的冻结快照作为评分器，无需额外大模型即可完成自压缩
- 无额外长度惩罚、精度奖励，完全靠对比信号引导模型自适应减少冗余推理
### 关键结果
在9个多模态基准（含MathVista、MMMU等）测试，相比最优基线ExOPD，COPD精度提升2.1pp的同时推理长度降低57%，单位token精度Acc@1K提升141%；训练GPU耗时相比传统OPD降低54.5%；自蒸馏变体COPSD在2B模型上精度提升3.5pp，推理长度压缩63.8%，Acc@1K提升194%。
> 高效蒸馏不需要强制约束输出长度，只需通过同状态下不同行为模式的对比信号，就能引导模型自动从现有输出分布中选择更高效的推理路径
