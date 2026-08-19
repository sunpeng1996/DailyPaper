---
title: 'Optimize Your Sampling: Tuned Diffusion Sampling with Bayesian Optimization'
title_zh: 基于贝叶斯优化的扩散模型定制化采样调度方法
authors:
- Travis Zhang
- Christian Belardi
- Justin Lovelace
- Jin Peng Zhou
- Saebyeol Shin
- Carla P. Gomes
- Kilian Q. Weinberger
affiliations:
- Cornell University
arxiv_id: '2608.18040'
url: https://arxiv.org/abs/2608.18040
pdf_url: https://arxiv.org/pdf/2608.18040
published: '2026-08-18'
collected: '2026-08-19'
category: Other
direction: 扩散模型采样效率优化
tags:
- Diffusion Model
- Bayesian Optimization
- Sampling Schedule
- Inference Acceleration
- Generative AI
one_liner: 将扩散采样时间步选择作为黑盒问题，用贝叶斯优化直接优化目标指标，无需额外训练即可大幅降低推理成本
practical_value: '- 电商AIGC业务（商品图生成、营销海报/素材生产、虚拟试穿渲染）可直接复用OYS调度替换原有扩散模型的默认采样步长，在损失不到11%生成质量的前提下将推理成本降低10倍，提升单卡吞吐

  - 无需修改原有扩散模型结构、无需额外训练，对已上线的生成式推荐多模态服务可零侵入替换采样逻辑，快速落地降本，兼容Euler、DPM-Solver++等主流采样器

  - 可将「直接面向业务目标做黑盒调度优化」的思路迁移到其他生成式服务的效率优化场景，比如LLM推理的KV cache淘汰策略优化、MoE模型的路由策略调优'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
扩散模型的迭代去噪生成需要多次执行大模型前向传播，推理成本极高；现有优化工作多聚焦采样器本身，对采样时间步调度的优化较少，且大多优化理论推导的代理指标，而非实际业务关注的生成质量指标。
### 方法关键点
OYS（Optimizing Your Sampling）框架将采样时间步选择定义为黑盒优化问题，直接用贝叶斯优化面向最终目标质量指标做调度优化；无需对扩散模型做任何额外训练，兼容Euler、DPM-Solver++等各类简单/复杂采样器，也适配蒸馏后的轻量化扩散模型。
### 关键结果
- 文生图任务效果优于默认调度和Align Your Steps方法，图像补全等任务也优于默认调度，定量和人工评估均验证效果
- 5步OYS调度可保留50步调度89%~94%的生成质量，推理成本降低10倍
