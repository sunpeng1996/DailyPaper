---
title: 'AdaFlash: Adaptive Speculative Decoding via On-Policy Distilled Diffusion
  Drafters'
title_zh: AdaFlash：基于On-Policy蒸馏扩散草稿的自适应投机解码
authors:
- Yu-Yang Qian
- Hao-Cong Wu
- Chen Chen
- Jiacheng Sun
- Zhenhua Dong
- Peng Zhao
- Zhi-Hua Zhou
affiliations:
- 南京大学
- 华为基础大模型部
arxiv_id: '2607.19223'
url: https://arxiv.org/abs/2607.19223
pdf_url: https://arxiv.org/pdf/2607.19223
published: '2026-07-21'
collected: '2026-07-22'
category: LLM
direction: LLM推理加速 · 投机解码优化
tags:
- Speculative Decoding
- Diffusion LLM
- On-Policy Distillation
- Inference Acceleration
- High Concurrency Serving
one_liner: 提出自适应扩散投机解码框架，解决扩散草稿模型高方差问题，高并发吞吐量较SOTA提升66%
practical_value: '- 部署LLM驱动的电商文案生成、Agent推理、Query改写服务时，可直接集成AdaFlash框架替换原有投机解码管线，高并发场景下吞吐量最高可提升66%，降低大模型服务成本

  - 生成式推荐、Semantic ID生成等任务遇到的小模型跨域泛化差、分布漂移问题，可复用reverse-KL+硬标签混合损失、逐元素梯度裁剪trick，提升小模型在业务分布上的适配效果

  - 业务场景下LLM服务需持续适配动态用户分布（如大促期Query变化），可借鉴异步训练-推理热更新管线，无需阻塞服务即可在线更新小模型参数，避免反复离线蒸馏的开销

  - 现有LLM serving引擎（如SGLang、vLLM）可复用变长请求调度策略，用EMA动态估计batch大小，提升高并发下GPU利用率，无需修改核心生成逻辑即可获得效率收益'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
扩散草稿模型（如DFlash）依靠双向注意力实现单步生成多token，比自回归草稿模型的投机解码效率更高，但双向注意力是双刃剑：并行生成能力的同时带来双重高方差问题，一是域级方差，不同任务域接受率波动大，跨域泛化差；二是token级方差，同一条草稿内不同位置接受概率差异大，固定验证长度会浪费大模型算力，高并发下性能甚至低于原生自回归解码，现有静态投机解码框架无法解决这两个问题。

### 方法关键点
- 针对域级方差，设计On-Policy蒸馏（OPD）算法，采用reverse-KL+硬标签交叉熵的混合损失，reverse-KL驱动小模型聚焦大模型高概率模式，硬标签提供低方差梯度；加入逐元素散度裁剪，抑制词汇表高差异条目带来的异常梯度，提升训练稳定性
- 针对token级方差，新增轻量自适应长度头，预测当前草稿的整体接受率，动态截断验证长度，仅将前k个高概率token送目标模型验证，减少无效计算；长度头用真实接受率做MSE损失在线更新，和草稿模型训练完全解耦
- 工程上实现异步训练-推理管线，训练侧消费推理侧的在线轨迹更新模型，参数热加载不阻塞推理；改造serving引擎支持变长验证长度，用EMA动态估计batch大小，提升高并发下GPU利用率

### 关键结果
在8个跨域数据集（数学、代码、对话等）、3个目标模型（稠密/MoE架构）上对比EAGLE-3、DFlash、OSD等SOTA方法，单请求场景下最高达5.3×原生自回归解码速度，128高并发场景下吞吐量比之前SOTA高66%，其他SOTA方法在高并发下速度甚至低于原生自回归解码，而AdaFlash仍保持稳定加速。

> 最值得记住：扩散模型的双向注意力是双刃剑，并行生成能力带来效率提升的同时，高方差问题必须结合在线自适应策略才能在生产环境发挥最大价值
