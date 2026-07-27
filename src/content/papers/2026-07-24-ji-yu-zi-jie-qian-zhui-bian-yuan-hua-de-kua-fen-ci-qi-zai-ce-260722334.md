---
title: Cross-Tokenizer On-Policy Distillation via Byte-Prefix Marginalization
title_zh: 基于字节前缀边缘化的跨分词器在策略蒸馏方法
authors:
- Hao Wang
- Kun Yuan
- Wenlin Zhong
- Minglei Zhang
- Han Xiao
- Ming Sun
- Honggang Qi
affiliations:
- University of Chinese Academy of Sciences
- KwaiKAT Team, Kuaishou
- Zhejiang University
- The Chinese University of Hong Kong
arxiv_id: '2607.22334'
url: https://arxiv.org/abs/2607.22334
pdf_url: https://arxiv.org/pdf/2607.22334
published: '2026-07-24'
collected: '2026-07-27'
category: Training
direction: 大语言模型 · 跨分词器知识蒸馏
tags:
- Knowledge Distillation
- On-Policy Distillation
- Cross-Tokenizer
- BPM
- LLM Training
one_liner: 提出字节前缀边缘化BPM方法，实现跨异构分词器的高效在策略知识蒸馏
practical_value: '- 业务侧需整合多模型能力到轻量化部署模型时，可复用BPM字节前缀对齐方案，无需统一师生模型分词器即可实现跨家族模型蒸馏，降低多模型路由部署成本

  - 生成类任务（如商品话术生成、详情页代码生成、Agent工具调用代码生成）蒸馏时，可直接复用全空格token掩码trick，避免分词器空格分割噪声被蒸馏进模型导致输出格式错误

  - 蒸馏损失选择优先选用forward KL，无需过多调优散度类型即可获得最优效果，减少业务侧蒸馏调优成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
不同开源大模型家族在推理、代码、工具调用等能力上互补，将多模型能力蒸馏到单一轻量化小模型是业务降本增效的核心需求，但传统在策略蒸馏要求师生模型共用分词器，限制了高能力教师的选择；现有跨分词器蒸馏方法要么丢失教师概率质量，要么将概率分配到语义无关的学生token，效果差强人意。
### 方法关键点
- 提出Byte-Prefix Marginalization（BPM），在共享字节空间对齐师生token分布：每个教师token的概率分配给字节是其前缀的最长学生token，聚合映射到同个学生token的概率，未匹配的概率放入显式残差类别，天然满足词汇完整性、字节对齐、质量守恒三个要求
- 针对学生token跨多个教师token的边界场景，用链式因子下界计算概率，保证整体概率质量守恒；训练时新增预计算的全空格行掩码，避免代码生成等场景下分词器的空格分割噪声被蒸馏，导致生成缩进错误、执行率下降
- 训练目标采用广义Jensen-Shannon散度，停止符单独处理，用forward KL回传梯度保证停止信号不会消失
### 关键实验
固定Qwen3.5-2B为学生模型，分别蒸馏Qwen3-32B、GLM-Z1-9B、MiniMax-M2.7三个不同分词器的教师模型，在3个数学、3个代码基准上测试：BPM比最强基线的六基准平均avg@8提升3.7~6.6个点，分别弥合33.5%、43.9%、34.4%的师生性能差距，效果超过离线蒸馏SeqKD方法。
### 核心结论
跨分词器蒸馏的核心是在字节空间做无损失的概率对齐，而非强行匹配token id或概率排序，同时要主动屏蔽无内容的噪声位置避免蒸馏退化
