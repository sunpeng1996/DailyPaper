---
title: 'RidgeFill: Training-Free Late-Layer Cache Fill for Faster Prefill'
title_zh: RidgeFill：无训练的LLM上层缓存填充方法加速Prefill阶段
authors:
- Dylan Johnston
- Robert P. Smith
affiliations:
- Independent researcher
arxiv_id: '2611.09709'
url: https://arxiv.org/abs/2611.09709
pdf_url: https://arxiv.org/pdf/2611.09709
published: '2026-11-06'
collected: '2026-11-09'
category: LLM
direction: LLM推理优化 · Prefill加速
tags:
- Prefill
- KV Cache
- Training-free
- Ridge Regression
- Inference Acceleration
one_liner: 无需训练的脊回归映射预测LLM上层输入，长上下文Prefill最高提速1.6倍，效果损失可忽略
practical_value: '- 部署LLM驱动的Agent、生成式推荐、智能客服等服务时，可直接集成RidgeFill降低长prompt（如拼接用户长期行为、商品库检索结果的prompt）的首token响应延迟，无需修改模型权重

  - 长上下文推荐/检索场景可复用「保留高注意力token、尾部最近token全量计算，其余token用线性映射预测」的策略，平衡推理速度和推荐/检索精度

  - 业务侧垂域小模型的推理加速可迁移无训练线性映射的思路，仅需少量垂域校准文本即可完成适配，适配成本远低于蒸馏、微调类加速方案

  - 推理服务工程优化可参考映射的双存储策略：硬件资源充足时将映射放VRAM最大化提速，资源紧张时从主机内存流式加载，仅损失少量速度即可节省大量显存'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
长prompt场景下LLM Prefill阶段需将所有token输入全部层计算，是首token延迟的核心瓶颈，现有上层跳过方案要么需要训练修改模型权重，要么精度损失过高，无法直接落地到已发布的现成模型部署。
### 方法关键点
- 选择分割层S，所有prompt token仅跑前S层，上层输入通过分割层输出的脊回归映射直接预测，无需迭代训练，仅需一次校准文本前向即可拟合映射参数
- 精度兜底：尾部数千token、高注意力权重token、特殊/稀有token全量跑所有层，其余token用预测值生成KV缓存，跳过MLP等冗余计算
- 针对带Gated DeltaNet的混合架构模型，新增值重缩放、终端状态修正两个无训练校正策略，进一步降低预测误差
### 关键结果
- A100部署Qwen3.8-27B，16K~120K prompt首token延迟提速1.25~1.31倍，RULER、LongBench v2评分仅降1.2~1.4分，95%置信区间包含0
- vLLM部署Qwen3.8-Flash-Next，9K~32K prompt首token延迟提速1.5~1.6倍，RULER needle任务得分99.8（满分100），新token困惑度仅上升2.65%
- 对比无训练baseline POP，同配置下填充区域RULER检索得分最高提升49.6分，效果和训练类方法SwiftKV相当
### 核心结论
Prefill是计算受限、解码是带宽受限，用Prefill阶段空闲带宽换计算量削减，无需训练即可在现成模型上实现显著的长上下文Prefill提速。
