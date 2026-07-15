---
title: 'Watermark Forensics for Generative Models: An Information-Theoretic Perspective'
title_zh: 生成模型输出水印取证的信息论视角分析
authors:
- Xiaoyu Li
- Zheng Gao
- Xiaoyan Feng
- Jiaojiao Jiang
- Yulei Sui
- Jiankun Hu
arxiv_id: '2607.13003'
url: https://arxiv.org/abs/2607.13003
pdf_url: https://arxiv.org/pdf/2607.13003
published: '2026-07-14'
collected: '2026-07-15'
category: LLM
direction: 大模型生成内容水印取证
tags:
- Watermark
- Generative AI
- Information Theory
- Forensics
- LLM Security
one_liner: 从信息论视角量化生成模型水印各取证能力的样本长度成本，给出首个多用户归因紧熵率定律
practical_value: '- 生成式推荐/LLM营销文案场景可基于信息剖面设计水印，平衡隐蔽性与可归因性，防止生成内容被滥用

  - 多用户水印归因可参考文中 surprisal 阈值化解码器设计，降低短文本（商品短标题、推广话术）归因的误判率

  - 需在推荐理由、搜索补全query中植入隐藏溯源payload时，可参考Θ(ℓ/h)样本长度结论提前做容量估算'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有生成模型水印大多仅支持AI生成内容检测，未量化归因、隐藏payload提取、篡改定位等高阶取证能力的实现成本，缺乏统一框架解释不同水印方案的能力边界。

### 方法关键点
提出信息剖面$\nu(t)=I(S;X_t\mid X_{<t})$作为核心度量，表征第t个token在给定前文时泄露的秘密信息S（用户ID、payload等）的信息量：检测能力仅依赖标记/未标记分布的距离，归因、payload提取能力依赖信息剖面总质量，定位能力依赖信息的分布密度。

### 关键结果数字
1. 无统计失真水印方案中，N个用户的归因所需样本长度为$\Theta(\log N/h)$（h为信源熵率），紧度达$(1+o(1))$因子，是首个多用户归因紧熵率定律
2. $\ell$比特payload提取所需样本长度为$\Theta(\ell/h)$
3. 存在$\Theta(\log N)$长度的固有间隙：文本可被检测为AI生成但无法归因
4. GPT-2、Pythia-410M、Qwen2.5上的实验完全匹配理论预测常数
