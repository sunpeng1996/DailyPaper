---
title: DiffusionGemma Technical Report
title_zh: DiffusionGemma技术报告：基于离散扩散的超高速开源大语言模型
authors:
- DiffusionGemma Team
- Adrien Ali Taïga
- James Assiene
- Daniele Calandriello
- Rahma Chaabouni
- João Gante
- Tamara von Glehn
- Nate Keating
- Chris Knutsen
- Martin Kukla
affiliations:
- Google DeepMind
arxiv_id: '2608.00146'
url: https://arxiv.org/abs/2608.00146
pdf_url: https://arxiv.org/pdf/2608.00146
published: '2026-07-30'
collected: '2026-08-04'
category: LLM
direction: 离散扩散大模型 · 低延迟推理优化
tags:
- Diffusion LLM
- MoE
- Low Latency Inference
- Discrete Diffusion
- Open Weight
one_liner: 基于Gemma4 MoE微调的开源离散扩散大模型，单H100生成速度达1500 token/s，刷新速度-质量帕累托最优边界
practical_value: '- 低延迟Agent/推荐文案/Query改写场景可直接复用DiffusionGemma替换传统AR LLM，单用户请求下推理速度提升4-7倍，大幅降低端到端延迟

  - 两阶段训练范式可迁移到垂直领域小扩散模型微调：先SFT适配双向扩散任务，再用采样蒸馏+RL联合优化质量和推理步数，仅需原AR模型10%的训练token预算

  - 熵约束采样+自适应停止trick可直接复用，根据任务复杂度动态调整推理步数，简单生成任务可进一步压缩延迟，复杂推理任务保留效果

  - 双模式（扩散+AR生成）路由思路可借鉴：业务场景按请求SLA动态切换生成模式，低延迟需求用扩散，高效果需求用AR，兼顾成本和体验'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
传统AR大模型逐token顺序解码的架构瓶颈导致单/低并发请求下严重内存带宽受限，算力利用率极低；现有speculative decoding方案最多仅能实现3~6 token/前向，速度提升上限明显。当前开源离散扩散大模型普遍存在能力弱、速度不达预期的问题，闭源扩散模型无法二次开发，行业缺少兼具强能力、超高速、开源可商用的离散扩散大模型。
### 方法关键点
- 基于Gemma 4 26B MoE（总参25.2B，激活参3.8B）微调，无需从零预训练，仅消耗原AR模型不到10%的训练token预算
- 两阶段训练管线：第一阶段SFT适配双向去噪任务，支持256 token块的并行迭代优化；第二阶段采样蒸馏+RL联合优化，同时提升生成质量、压缩去噪步数
- 推理采用熵约束采样+线性温度退火+自适应停止策略，平均仅需12次去噪前向即可完成256 token块生成，平均输出20 token/前向
- 保留原AR模型的多模态、长上下文、思考模式能力，同时兼容AR生成模式，仅存在轻微性能衰减
### 关键结果
- 覆盖数学推理、代码、知识、多模态、Agent任务等多维度benchmark，对比基线包括Gemma 4全系列、LLaDA 2.1、Nemotron Diffusion、闭源Mercury 2
- 单NVIDIA H100 FP8 batch=1下生成速度达1500 token/s，是带MTP优化的Gemma 4 AR的4.8倍，普通AR的7.1倍；batch<32的低并发场景下总吞吐量和单用户速度均优于AR模型
- 刷新扩散大模型速度-质量帕累托边界，效果接近闭源Mercury 2，速度是其2.5倍

**最值得记住的结论**：离散扩散大模型通过块级并行解码将LLM推理从内存bound转向计算bound，在低延迟场景的收益已经足够落地，是对传统AR生成范式的有力补充。
