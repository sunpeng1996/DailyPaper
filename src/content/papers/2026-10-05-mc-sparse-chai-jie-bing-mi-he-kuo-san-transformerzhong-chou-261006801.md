---
title: 'MC-Sparse: Deconstructing and Closing the Dense-Sparse Attention Gap in Diffusion
  Transformers'
title_zh: MC-Sparse：拆解并弥合扩散Transformer中稠密-稀疏注意力差距
authors:
- Jiarui Chen
- Zeqiang Lai
- Jiangshan Wang
- Ziheng Ouyang
- Ye Huang
- Xiangyu Yue
- Cewu Lu
- Chunchao Guo
affiliations:
- Fudan University
- Tencent HY
- MMLab, CUHK
- Nankai University
- Peking University
arxiv_id: '2610.06801'
url: https://arxiv.org/abs/2610.06801
pdf_url: https://arxiv.org/pdf/2610.06801
published: '2026-10-05'
collected: '2026-10-06'
category: LLM
direction: 大模型推理 · 稀疏注意力加速
tags:
- Sparse-Attention
- Diffusion-Transformer
- Inference-Optimization
- Training-Free
- KV-Cache
one_liner: 训练免微调的稀疏注意力框架，在无显著质量损失前提下将DiT推理速度提升最高2.32倍
practical_value: '- 电商场景下的商品图/营销短视频生成等DiT类任务可直接复用MC-Sparse免训练框架，在不损失生成质量前提下降低推理延迟，提升在线服务吞吐量

  - 可借鉴跨步骤缓存query分组、KV索引、稠密-稀疏残差的设计思路，优化长序列RAG、多轮Agent对话的KV cache复用策略，减少重复计算开销

  - tile对齐的快速PDDP查询分组方法可迁移到推荐系统多兴趣用户建模、候选集粗排聚类分块场景，平衡聚类质量与GPU执行效率'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
扩散Transformer（DiT）已成为视频、3D资产等高分辨率内容生成的主流骨干，但长序列场景下稠密注意力的二次计算复杂度成为推理核心瓶颈。现有稀疏注意力方案大多采用块粒度选择，在高稀疏度下会显著降低生成保真度，始终存在效率与质量的 trade-off 缺口，亟需免训练、无质量损失的稀疏注意力加速方案。
### 方法关键点
- 通过对照oracle实验拆解出稀疏注意力质量损失的三大来源：结构绑定误差（块级选择强制绑定无关token、同组query共享选择结果）、选择误差（近似评分选块不准）、丢弃尾误差（被丢弃的低权重token仍有非零贡献）
- 采用锚点步+复用步的两级流程：仅在锚点步执行一次稠密注意力计算，生成tile对齐的等规模query分组、精确的token级KV选择索引、稠密与稀疏注意力输出残差，后续复用步直接复用上述元数据，仅计算当前Q/K/V
- 配套实现快速PDDP查询聚类、双通精确KV选择、token级稀疏注意力内核三大工程优化，保障GPU执行效率，避免非对齐计算的资源浪费
### 关键实验
在视频生成（Minimax-H3、混元视频、Wan2.1）、3D资产生成两类任务上对比Sol-Attn、PISA、SVG-EAR等主流稀疏注意力基线：15%注意力密度下，Minimax-H3 768P视频生成实现1.80×加速，3D资产生成实现2.32×加速，PSNR、SSIM等保真度指标均显著优于基线，无肉眼可察觉的质量损失。
### 核心结论
稀疏注意力的优化不能只关注选择精度，降低结构绑定损耗、补偿丢弃尾贡献、利用跨步骤时间冗余复用元数据是实现无损加速的核心路径
