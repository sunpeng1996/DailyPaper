---
title: Total Variation Distance Estimation in Autoregressive Models
title_zh: 自回归模型的总变分(TV)距离估计算法
authors:
- Eric Price
- Kevin Tian
- Zhiyang Xun
- Yusong Zhu
affiliations:
- University of Texas at Austin
arxiv_id: '2607.19510'
url: https://arxiv.org/abs/2607.19510
pdf_url: https://arxiv.org/pdf/2607.19510
published: '2026-07-21'
collected: '2026-07-23'
category: Eval
direction: LLM推理一致性评估 · TV距离估计
tags:
- Total Variation Distance
- Autoregressive Model
- LLM Inference
- Distribution Testing
- Query Complexity
one_liner: 提出三种访问模式下自回归模型TV距离估计算法，复杂度优于SOTA，可用于LLM推理栈一致性校验
practical_value: '- LLM推理优化（量化、KV cache优化、引擎替换）上线前的一致性校验，优先用TV距离替代KL散度，避免KL因支持集不相交出现无穷大、无法量化微小差异的问题

  - 白盒场景下直接复用文中O(n/ε²)复杂度的logit访问TV估计算法，效率远高于采样法，适合内部推理栈迭代的快速校验

  - 黑盒场景下用前缀采样+多层蒙特卡洛方差缩减的算法，相比现有方法query量降低1-2个数量级，可用于闭源LLM服务的一致性审计

  - 生成式推荐场景可复用该方法校验模型迭代前后的输出（文案、候选item）分布一致性，避免上线后分布偏移导致业务指标波动'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
同权重LLM部署时，推理引擎、量化策略、batching逻辑、kernel实现都会导致输出分布产生显著差异，现有常用的KL散度度量存在支持集不相交时无穷大、无统一近似保证的问题，无法可靠量化分布差异，亟需可落地、有理论保证的分布距离度量方法。
### 方法关键点
- 定义三类LLM访问模式：仅采样访问、白盒logit访问、带噪声的logit访问，分别对应闭源API、内部白盒模型、生产环境带随机噪声的推理服务场景
- 针对三类模式分别推导TV距离估计的上下界：采样访问下复杂度为Õ(n²K/ε²)，较之前SOTA的Õ(n³m/ε⁵)大幅优化；logit访问下复杂度为O(n/ε²)且为紧界；带噪声logit访问下可在两类复杂度间平滑插值
- 设计多层蒙特卡洛方差缩减方案，解决噪声场景下估计方差大、query量过高的问题，可分离真实分布差异与推理噪声
### 关键结果
- 实测5款Qwen系列模型、3种注意力后端的推理噪声，生产环境batching会引入明显logit噪声，σ²远小于top-k截断的K值，噪声场景算法复杂度远低于纯采样法
- 测试vLLM和SGLang部署同权重Qwen3-0.6B的分布差异，算法可准确区分自噪声（约0.016）、不同后端的真实差异（FlashAttention-2与cuDNN的TV约0.034），重复采样可分离噪声与真实偏差

最值得记住的一句话：衡量同权重LLM不同部署方案的输出分布一致性时，TV距离是比KL散度更稳定、可解释、有理论保证的选择，配套估计算法已可落地使用。
