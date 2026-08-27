---
title: 'When Pruning Meets Interpretability: Preserving Sparse Autoencoder Robustness
  in LLMs'
title_zh: 兼顾剪枝与可解释性：保留大语言模型稀疏自编码器鲁棒性
authors:
- Suchit Gupte
- Xueru Zhang
- Mohammad Mahdi Khalili
affiliations:
- The Ohio State University
arxiv_id: '2608.25941'
url: https://arxiv.org/abs/2608.25941
pdf_url: https://arxiv.org/pdf/2608.25941
published: '2026-08-26'
collected: '2026-08-27'
category: LLM
direction: 大语言模型剪枝 · SAE可解释性保留
tags:
- Sparse Autoencoder
- LLM Pruning
- Interpretability
- Perturbation Theory
- WANDA
- SparseGPT
one_liner: 推导剪枝对SAE的扰动边界，提出分层稀疏分配策略，剪枝压缩同时保留SAE可解释性
practical_value: '- 若业务中用SAE做LLM语义特征抽取、可解释性分析、干预调控（如推荐场景用户/商品特征解耦、Agent工具调用逻辑可解释），剪枝压缩LLM时优先选择WANDA或SparseGPT，避免使用MAGNITUDE剪枝，可将SAE干预有效性的下降控制在25%以内，远优于MAGNITUDE剪枝60%以上的下降幅度。

  - 可复用分层稀疏分配思路做LLM剪枝优化：给LLM中间层分配更低的稀疏度，早期/晚期层分配更高稀疏度，相同平均压缩率下可降低perplexity，同时保留SAE的可解释性功能，适合需要压缩部署LLM且依赖可解释性的业务场景。

  - 评估剪枝后SAE的有效性时，不能仅看重建MSE、KL散度等聚合指标，需补充Feature Absorption、SCR、TPP三类维度的验证，避免出现聚合指标达标但实际特征失效、干预无效的隐性问题。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Sparse Autoencoder（SAE）是当前LLM机制可解释性的核心工具，而剪枝是LLM落地部署的标准压缩手段，但现有剪枝方法仅关注下游任务效果，完全忽略对预训练SAE功能的影响。SAE失效通常是隐性的，无法通过常规语言建模基准检测，此前没有理论框架解释不同剪枝方法对SAE的影响差异，也没有兼顾压缩率与SAE功能保留的剪枝优化方案。

### 方法关键点
- 理论上提出**扰动能量**（协方差加权的扰动范数）作为SAE退化的核心度量，证明SAE重建误差上界由扰动能量、SAE的Lipschitz常数共同决定。
- 明确三类剪枝方法的理论差异：MAGNITUDE剪枝忽略激活协方差，诱导的扰动能量最大；WANDA采用协方差对角近似，扰动能量次之；SparseGPT直接最小化扰动能量，对SAE的友好度最高。
- 发现LLM中间层对剪枝的敏感度远高于早期和晚期层，基于此提出分层稀疏分配策略：给早期/中间层分配更低的稀疏度，晚期层分配更高稀疏度，在相同平均压缩率下实现更好效果。

### 关键结果数字
- 实验覆盖pythia-70m、gemma-2-2b、gemma-2-9b、mistral-7b共4个主流LLM的预训练SAE，在25%/40%/50%三个稀疏度下验证。
- 50%稀疏度下，MAGNITUDE剪枝导致SAE的SCR（干预有效性）最高下降60%、TPP（干预选择性）最高下降80%，而WANDA和SparseGPT的对应下降幅度仅为15%~25%。
- 分层稀疏分配策略在50%平均稀疏度下，将gemma-2-2b的perplexity从21降至14.8（WANDA）、从19.8降至14（SparseGPT）。

**最值得记住的一句话**：对需要保留SAE可解释性的LLM剪枝场景，优先选择激活感知的剪枝方法，同时给中间层分配更低的稀疏度，可在压缩部署成本的同时避免可解释性工具隐性失效。
