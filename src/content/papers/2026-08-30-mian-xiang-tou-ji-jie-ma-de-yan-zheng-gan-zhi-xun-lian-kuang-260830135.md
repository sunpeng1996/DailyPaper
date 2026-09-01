---
title: Verification-Aware Training for Speculative Decoding
title_zh: 面向投机解码的验证感知训练框架VAT
authors:
- Geonmo Gu
- Byeongho Heo
- HeeJae Jun
- Yoohoon Kang
- Sangmin Lee
- Sangdoo Yun
- Dongyoon Han
affiliations:
- NAVER AI Lab
- NAVER AI Search Platform
- Korea University
arxiv_id: '2608.30135'
url: https://arxiv.org/abs/2608.30135
pdf_url: https://arxiv.org/pdf/2608.30135
published: '2026-08-30'
collected: '2026-09-01'
category: Training
direction: LLM推理加速 · 投机解码训练优化
tags:
- Speculative Decoding
- Inference Acceleration
- Training Objective
- LLM
- Draft Model
one_liner: 提出仅修改训练目标的验证感知训练插件，提升投机解码的接受长度与推理速度
practical_value: '- 业务侧用LLM做生成式推荐文案、对话Agent实时回复时，可直接将VAT作为插件接入现有EAGLE/DFlash等投机解码框架的训练流程，无需修改推理逻辑即可获得5%~10%的端到端速度提升，适配latency敏感的实时场景

  - 训练目标设计思路可迁移至多步生成类推荐任务：比如Semantic ID序列生成、多轮query推荐等，只要推理时存在"前序错误导致后续结果作废"的规则，都可模拟截断逻辑、给有效前缀加权、加辅助头预测截断位置，对齐训练与推理分布

  - 工程落地时可额外利用VAT的验证头做推理早停：根据验证头的接受概率预测提前截断无效候选，进一步降低推理算力消耗，无需修改原有模型结构'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有投机解码的草稿模型训练采用固定位置权重的token级模仿，未对齐推理时的顺序验证逻辑——只要某一位置被目标模型拒绝，后续所有候选都会被丢弃，导致训练目标与推理实际收益脱节，无法最大化接受长度这个核心加速指标。
### 方法关键点
- 训练时实时模拟目标模型的验证过程，得到每个样本的首次拒绝位置`k*`及各位置的接受标签
- 新增轻量验证头（单全连接层）作为辅助目标，预测每个位置是否通过顺序验证，梯度反向传播优化草稿模型的隐藏表示
- 验证自适应加权：`k*`之前的位置损失权重保持1，`k*`之后的位置沿用原衰减schedule但锚定`k*`作为衰减起点，动态适配每个样本的验证结果
- 最终损失结合软标签+硬标签的加权交叉熵、验证头损失，仅修改训练目标，不改动推理逻辑
### 关键结果
在Qwen3-4B/8B、LLaMA-3.1-8B三个目标模型上，对接EAGLE-3、DFlash两种主流投机解码框架，在数学、代码、聊天三类benchmark测试：平均接受长度最高提升11.4%，端到端墙钟速度最高提升8.7%；训练overhead仅1.2%（EAGLE-3）到6.1%（DFlash），几乎可忽略。
> 最值得记住：对于多步顺序生成任务，训练目标必须对齐推理时的实际收益规则，而非单纯做单步token级模仿，才能最大化落地收益
