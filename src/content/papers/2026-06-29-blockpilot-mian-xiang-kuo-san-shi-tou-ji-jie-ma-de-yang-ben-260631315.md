---
title: 'BlockPilot: Instance-Adaptive Policy Learning for Diffusion-based Speculative
  Decoding'
title_zh: BlockPilot：面向扩散式投机解码的样本自适应策略学习
authors:
- Hao Zhang
- Yiming Hu
- Yong Wang
- Mingqiao Mo
- Xin Xiao
- Xiangxiang Chu
affiliations:
- AMAP, Alibaba Group
arxiv_id: '2606.31315'
url: https://arxiv.org/abs/2606.31315
pdf_url: https://arxiv.org/pdf/2606.31315
published: '2026-06-29'
collected: '2026-07-01'
category: LLM
direction: LLM推理优化 · 扩散式投机解码
tags:
- Speculative Decoding
- Diffusion LLM
- Inference Acceleration
- Policy Learning
- Dynamic Decoding
one_liner: 基于预填充阶段最后token分布预测最优解码块大小，为扩散式投机解码带来最高4.2×无损加速
practical_value: '- 业务侧用LLM做商品文案生成、智能客服、Agent决策的场景，可直接将BlockPilot接入现有扩散式投机解码 pipeline，无需修改主干模型即可获得10%+推理提速，有效降低大模型部署成本

  - 利用预填充阶段最后token的全上下文分布做轻量决策的思路可迁移到生成式推荐场景：根据query/用户画像的上下文确定性，动态调整生成候选item的数量，平衡召回效率和效果

  - 最优超参数局部性结论可复用：无需做全局超参搜索，仅在训练值的±3范围内枚举候选即可覆盖99%以上的最优情况，大幅降低调优和监督数据构造成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
扩散式投机解码是当前LLM无损推理加速的SOTA范式，通过块级扩散并行生成多token再统一验证，大幅提升解码效率。但现有方案采用固定推理块大小，忽略不同输入的上下文确定性差异：确定性强的输入可支持更大块的并行生成，不确定性高的输入用大块会导致错误累积、接受率下降，固定块大小的设计无法适配输入特性，加速潜力未被充分释放。
### 方法关键点
- 验证最优块大小的局部性：99%以上样本的最优块大小集中在训练阶段使用的块大小±3范围内，将原本的全局搜索问题转化为有限离散空间的分类任务，大幅降低难度
- 轻量决策模块设计：直接取预填充阶段最后一个token的原始预测分布作为输入（聚合了全上下文信息），用2层MLP做分类预测最优块大小，仅在预填充后执行一次，推理开销仅7ms左右
- 离线监督数据构造：对每个训练样本枚举局部候选块大小的实际接受长度，取最优值作为监督标签训练分类器，无需修改原有draft模型、target模型及验证流程，可无缝接入现有框架
### 关键实验
测试覆盖Qwen3-4B/8B、Llama3.1-8B-Instruct、Qwen3-Coder-30B四类不同规模、不同领域的模型，基准数据集覆盖数学推理、代码生成、对话三类场景，对比EAGLE-3、不同固定块大小的DFlash baseline。温度=1时在Qwen3-4B上实现4.20×加速，平均接受长度达5.92，比最强固定块DFlash基线提升10.5%的加速比，所有模型、所有场景下性能均优于对比基线。
### 核心洞察
LLM推理优化不仅可以靠模型结构改进，动态适配输入特性的解码策略能以极低 overhead 带来显著的效率提升
