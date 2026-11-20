---
title: 'One Schedule Does Not Fit All: Adaptive Inference Schedules for Diffusion
  Language Models'
title_zh: 扩散语言模型自适应推理调度：为不同任务匹配最优去噪策略
authors:
- Rabimba Karanjai
- Linsey Pang
- Hemanth Hegadehalli Madhavarao
- Richard Williamson
- Uma Kona
- Prakhar Mehrotra
affiliations:
- PayPal Inc.
arxiv_id: '2611.25895'
url: https://arxiv.org/abs/2611.25895
pdf_url: https://arxiv.org/pdf/2611.25895
published: '2026-11-19'
collected: '2026-11-20'
category: LLM
direction: 扩散大语言模型 · 推理调度优化
tags:
- Diffusion LLM
- Inference Optimization
- Sampling Schedule
- Risk Control
- Adaptive Computation
one_liner: 提出带误差保障的TCDA框架，为扩散语言模型匹配成本最低的质量无损推理调度
practical_value: '- 电商/广告文案生成场景若使用Diffusion LLM，可直接复用TCDA校准逻辑，上线前用百级样本验证候选采样策略，无需用默认全步长调度，强条件生成任务（如给定属性写商品标题）可获3倍+加速且无质量损失

  - 评估生成加速策略时必须加入退化护栏（输出长度偏差、重复率、distinct-2等），不能仅看自动效用指标，避免出现生成循环、语义重复等bad case，保障电商文案合规性与用户体验

  - 做Diffusion LLM推理优化无需过度关注隐空间残差指标，优先统计token稳定时机：强条件生成任务中80%+token在1/3步长时已确定，提前解码即可获得极高加速比

  - 线上部署ELF类带随机时间网格的扩散模型时，必须替换为确定性分位数网格，避免不同请求的生成质量波动，符合电商/推荐场景的效果稳定性要求'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
扩散语言模型（如ELF、LLaDA）默认采用固定去噪调度，但不同任务的最优调度差异极大：XSum摘要任务跑19步效果优于全64步，同策略在WMT翻译任务掉35个chrF点，GSM8K数学题提前半步长掉52个准确率点，固定调度要么浪费算力要么降低生成质量，亟需可落地的质量保障型调度选择方案。

### 方法关键点
- TCDA（任务校准去噪分配）是认证后部署的规则，不属于新采样器，可接入任意候选采样器（提前解码、状态复用粗网格、自适应置信度解码等）
- 核心采用单侧bootstrap联合认证机制：同时验证候选调度的效用偏差在容忍阈值ε内，且满足退化护栏（输出长度、重复率、distinct-2等），错误部署概率渐近不超过αu+αg（默认αu=0.04，αg=0.01）
- 以denoiser评估次数（NFE）为调度成本衡量标准，优先选择满足条件的最低成本调度，不满足则自动fallback到全步长调度

### 关键结果
在2类模型（ELF-B/M/L、LLaDA-8B）、7个数据集上验证：ELF-B在XSum上获3.37×NFE减少、3.28×端到端加速，WMT14上获2×加速，错误认证率低于2%；LLaDA-8B在WMT14上获8×NFE减少、7.5×加速，GSM8K上获4.1×加速，0错误认证；采用127候选调度的扩展库时，XSum加速比可达6.75×，WMT14达3.8×。

### 核心结论
扩散语言模型的最优推理调度由任务、模型、采样器共同决定，token的稳定时机而非隐空间残差决定了加速策略的安全性。
