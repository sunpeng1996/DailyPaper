---
title: Telescopic Language Models
title_zh: 伸缩式语言模型：单次训练生成全深度连续可用的嵌套大模型
authors:
- Zhilin Guo
- Boqiao Zhang
- Hakan Aktas
- Kyle Fogarty
- Nursena Koprucu Aslan
- Wenzhao Li
- Canberk Baykal
- Albert Miao
- Siyu Hong
- Yixiao Liu
affiliations:
- University of Cambridge
- University of British Columbia
- Google
arxiv_id: '2609.35769'
url: https://arxiv.org/abs/2609.35769
pdf_url: https://arxiv.org/pdf/2609.35769
published: '2026-09-28'
collected: '2026-09-29'
category: Training
direction: 大模型训练 · 弹性可部署LLM构建
tags:
- Nested LLM
- Elastic Inference
- Training Efficiency
- Cost Optimization
- Matryoshka Architecture
one_liner: 采用带全锚点的随机前缀监督训练嵌套Transformer，单次训练得到任意深度可用的连续LLM，无额外推理开销
practical_value: '- 搭建多 latency 档位的端侧/云侧 LLM 服务（如电商个性化文案生成、query 改写）时，可复用 TLM 训练策略，单次训练即可覆盖从低延迟轻量版到高性能全量版的所有档位，无需多轮训练或后压缩，大幅降低训练成本

  - 端侧推荐场景部署 LLM 时，可基于 TLM 框架根据设备算力动态切分模型深度，无需维护多套模型权重，降低端侧包体积与部署复杂度

  - Agent 任务调度场景可将 TLM 作为弹性基座，简单任务调用浅层前缀降低推理耗时，复杂任务调用全量模型保证效果，平衡全链路 latency 和效果'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有 LLM 部署需针对不同算力/latency 预算单独训练或压缩模型，成本高；嵌套式 Matryoshka 模型仅监督固定出口，非出口深度的模型完全不可用，PPL 飙升至 10²~10⁵，无法实现连续的预算-效果 tradeoff，亟需单次训练即可覆盖全预算档位的方法。

### 方法关键点
- 复用 MLMS 嵌套 Transformer 架构，每层宽度随深度递增，任意深度前缀都是独立完整的 LLM，无需修改架构
- 采用带全锚点的随机前缀监督损失：每步随机采样一个深度前缀，计算该前缀的 next-token 交叉熵损失，同时叠加全量模型的损失，仅需 2 次前向后向传播，推理无额外开销
- 可通过调整前缀采样分布调整 tradeoff：均匀采样覆盖全深度连续档位，集中采样到固定深度可对标固定出口模型的效果

### 关键实验
基于 200M 参数 MLMS 架构，用 20B FineWeb-Edu tokens 训练，对比 MLMS、独立训练的 vanilla 模型：
1. 单次训练即可获得 20 个全深度可用的 LLM，非出口深度 PPL 从 MLMS 的 10²~10⁵ 降到 15~81 的连续区间，质量-预算曲线下面积（AULB）相对降低 43%~44%
2. 全量模型效果与 MLMS 持平，训练 GPU 成本比 MLMS 低 12%，比独立训练 3 个档位模型低 41%
3. 部署覆盖度 LODA 指标相对 MLMS 提升 1.8 倍，可支持任意未提前预设的 latency 预算

### 核心结论
嵌套弹性模型的连续可用性瓶颈来自训练目标而非架构，仅需随机采样前缀加全锚点监督，即可零推理开销获得全深度连续可用的模型序列。
