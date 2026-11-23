---
title: Non-penetrating World Models
title_zh: 防穿透的交互视频世界模型
authors:
- Yuhang Dai
- Yinwei Wu
- Ziyue Lin
- Han Ji
- Xingyi Yang
affiliations:
- Learning & Generation Lab, The Hong Kong Polytechnic University
arxiv_id: '2611.27963'
url: https://arxiv.org/abs/2611.27963
pdf_url: https://arxiv.org/pdf/2611.27963
published: '2026-11-19'
collected: '2026-11-23'
category: Agent
direction: Agent世界模型 · 物理约束优化
tags:
- World Model
- Diffusion Transformer
- Physical Constraint
- Benchmark
- Zero-shot Learning
one_liner: 提出评估世界模型物理穿透的基准与轻量化修复框架，将平均违规率从74%降至16%
practical_value: '- 可复用「冻结大模型+轻量头部」的低成本优化范式：针对现有生成类模型已编码但未输出的隐层信息，加小检测头即可修复特定缺陷，无需全量微调

  - 「异常检测+意图保留替换」的思路可迁移到电商AR/3D交互场景：解决虚拟试穿、AR逛店中人物/商品穿模、穿透场景物体的生成错误问题

  - 零样本泛化的验证逻辑可参考：优化策略无需针对新场景重训，可直接适配不同视角、动态交互对象等业务非标场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有交互视频世界模型普遍存在物体穿透物理障碍的严重缺陷，暂无公开基准专门评估该问题，全量微调修复成本极高，且未利用模型已有的隐层信息。
### 方法关键点
1. 推出NoPeBench benchmark，专门量化评估世界模型对物理障碍物的响应准确率；
2. 验证发现Diffusion Transformer（DiT）的隐层状态已完整编码穿透预测所需信息，无需改动原模型权重；
3. 提出NoPeWorld轻量化框架：在冻结DiT的隐层上训练小预测头判断动作安全性，将不安全动作替换为最大程度保留原意图的安全动作。
### 关键结果
在6款开源世界模型上平均物理违规率从74%降至16%，且具备零样本泛化能力，可直接适配开放域图像、第三人称视角、移动障碍物三类场景。
