---
title: 'SpecFold: Folding Multi-Branch Redundancy for Faster Speculative Decoding
  in Diffusion Language Models'
title_zh: SpecFold：折叠多分支冗余加速扩散大语言模型推测解码
authors:
- Chung-En Ho
- Weiyu Sun
- Cheng-Jhih Shih
- He Li
- Yong Liu
- Yingyan Celine Lin
affiliations:
- Georgia Institute of Technology
arxiv_id: '2610.04875'
url: https://arxiv.org/abs/2610.04875
pdf_url: https://arxiv.org/pdf/2610.04875
published: '2026-10-05'
collected: '2026-10-10'
category: LLM
direction: LLM推理优化 · 扩散LLM推测解码
tags:
- Diffusion LLM
- Speculative Decoding
- Inference Acceleration
- Triton Kernel
- Computation Reuse
one_liner: 算法-系统协同设计复用扩散LLM多分支推测解码冗余计算，最高提速1.99倍无精度损失
practical_value: '- 多分支候选并行验证场景（如生成式推荐多候选打分、Agent多工具调用路径校验）可直接复用token级残差门控逻辑，仅重计算差异位置的QKV与FFN，大幅降低batch内冗余计算开销

  - 基于Triton实现的稀疏计算打包、跨分支状态复用、折叠链自动寻址思路可直接迁移到LLM推理服务，提升大模型部署的吞吐性价比

  - 扩散LLM的解码优化经验可复用在电商长文案、商品描述、个性化营销内容批量生成场景，通过多分支推测+冗余折叠平衡生成速度与效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
扩散大语言模型（DLLM）的多分支推测解码可通过单步前向同时验证主分支与多个候选分支，大幅降低所需的去噪迭代次数，但传统稠密验证方案会随分支数增长线性提升单步计算成本，此前优化多聚焦跨步骤的时序冗余，未利用单步验证内多分支间的计算冗余，导致实际吞吐增益被额外开销抵消。

### 方法关键点
- 算法层：引入token级残差门控，当子分支与父分支对应位置隐状态相对残差低于阈值δ时，直接复用父分支的QKV、FFN计算结果，仅重计算差异位置；通过增量修正保证双向注意力计算精度，各分支保留独立残差流避免候选多样性损失
- 系统层：基于Triton实现定制内核，打包跨分支的重计算位置，避免冗余张量实例化，支持折叠链自动寻址、共享前缀KV缓存零拷贝复用
- 完全兼容现有DLLM推测策略与时序缓存优化，无需修改模型权重或候选分支构造逻辑

### 关键实验
在Fast-dLLM-v2、Nemotron-Labs-Diffusion两个DLLM系列共5个模型（1.5B~14B）、GSM8K/MATH/HumanEval/MBPP/IFEval共5个基准上测试，对比基线Spiffy与原生解码：最高比Spiffy提升1.64倍吞吐，最高比原生解码提升1.99倍吞吐，δ阈值设为0.1时精度损失可忽略，分支数越多优化增益越显著。

### 最值得记住的一句话
多分支并行验证场景下，单步内跨分支的计算冗余是比跨步骤时序冗余更易被忽视的优化空间，细粒度的计算复用可在不损失效果的前提下大幅提升推理吞吐。
