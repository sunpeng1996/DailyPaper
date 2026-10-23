---
title: 'OneLatent: Latent Reasoning for Efficient Foundation Recommendation Models'
title_zh: OneLatent：面向推荐基础模型的高效隐式推理框架
authors:
- Hao Jiang
- Peiru Du
- Pengfei Yao
- Mengting Li
- Siyuan Lou
- Kuo Cai
- Sheng Yu
- Qiang Luo
- Jian Liang
- Ruiming Tang
affiliations:
- Kuaishou Technology
arxiv_id: '2610.30675'
url: https://arxiv.org/abs/2610.30675
pdf_url: https://arxiv.org/pdf/2610.30675
published: '2026-10-22'
collected: '2026-10-23'
category: GenRec
direction: 生成式推荐 · 隐式推理优化
tags:
- GenRec
- FRM
- Latent Reasoning
- CoT
- Semantic ID
one_liner: 将显式CoT蒸馏为3个可学习隐式推理token，提升FRM精度的同时实现17倍推理吞吐量提升
practical_value: '- 可复用隐式token蒸馏范式：将大模型显式CoT监督蒸馏为固定数量的隐式推理token，既保留推理增益又避免显式生成的推理开销，适合GenRec落地优化

  - MV-ACoT构造方法可直接复用：从意图探索、正样本匹配、归因三个视角构造CoT监督，自适应调整推理长度，比固定模板CoT质量更高

  - 工业级部署架构可参考：将FRM作为独立召回通道，基于用户行为优先级异步更新、缓存结果，避免FRM同步推理占用请求路径latency，适配大流量生产环境

  - 课程式训练策略可迁移：从高活用户到低活用户分阶段微调，再混合常规推荐与隐式推理任务训练，兼顾模型泛化性与推理能力'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有推荐基础模型（FRM）采用显式CoT推理存在两大痛点：一是冗长推理文本生成带来极高推理开销，ROI极低；二是固定模板CoT容易忽略用户短期上下文兴趣，推理错误会传播到最终推荐结果，难以适配工业级大流量场景。

### 方法关键点
- 提出MV-ACoT多视角自适应CoT构造方法，从意图探索、正样本评估、交互归因三个视角生成高质量CoT监督，自动适配每个样本的推理复杂度，减少冗余推理
- 三阶段隐式token对齐范式：先单视角、再多视角对齐隐式token到CoT监督，最后对齐到推荐目标Semantic ID，无额外模块引入
- 课程式后训练：先从高活到低活用户分阶段微调推荐能力，再按1:1混合常规推荐与隐式推理任务训练，同时支持两种推理模式
- 工业级服务架构：将FRM作为独立召回通道，基于用户价值/行为强度异步触发推理、缓存结果，推理链路不占用在线请求关键路径

### 关键实验
实验覆盖快手本地生活工业数据集、公开快手LLM-Rec基准，对比传统序列推荐、生成式推荐、显式CoT FRM三类基线。核心结果：工业数据集上SID@64相对显式Think变体提升17.44%，相对No-Think变体提升9.33%，推理吞吐量是显式CoT的17.49倍；线上A/B测试快手本地生活广告场景收入提升9.6%。

最值得记住的一句话：显式CoT完全可以作为训练监督而无需在推理阶段生成，通过隐式token蒸馏可同时实现精度提升与效率数量级优化，是FRM落地的可行路径
