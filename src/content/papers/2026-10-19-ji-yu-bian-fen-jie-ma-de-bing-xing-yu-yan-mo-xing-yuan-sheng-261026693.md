---
title: Parallel Language Models via Variational Decoding
title_zh: 基于变分解码的并行语言模型：原生支持多token并行生成
authors:
- Felix Draxler
- Robin C. Geyer
- Daniel Geyfman
- Farrin Marouf Sofian
- Justus Will
- Philipp Hildebrandt
- Giosue Migliorini
- Prakhar Srivastava
- Gagan Sai Trinadh Duggaraju Peddiraju
- Kushagra Pandey
affiliations:
- University of California, Irvine
- ETH Zurich
- Charité Berlin
- Hasso Plattner Institute
arxiv_id: '2610.26693'
url: https://arxiv.org/abs/2610.26693
pdf_url: https://arxiv.org/pdf/2610.26693
published: '2026-10-19'
collected: '2026-10-20'
category: LLM
direction: LLM推理加速 · 并行生成
tags:
- Parallel Decoding
- LLM Inference Acceleration
- Variational Training
- Multi-token Generation
one_liner: 提出变分训练的并行语言模型，推理速度比同质量自回归模型高2.3-5.7倍
practical_value: '- 低延迟LLM服务场景（电商实时客服Agent、搜索query实时改写、推荐理由即时生成）可直接复用PLM训练框架，在不损失生成质量的前提下降低推理延迟2-5倍，提升用户体验

  - 训练侧的自蒸馏+权重共享设计、推理侧的块并行验证策略可直接迁移到垂直领域小参数LLM的加速优化，比如电商专属垂类LLM的微调与部署

  - 多token并行生成的变长块策略可与现有vLLM、KV cache优化结合，进一步提升大流量推荐/广告场景下的LLM服务吞吐，降低部署成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
自回归LLM每轮前向仅生成1个token，推理延迟随模型规模放大显著，现有投机解码受限于小模型draft质量上限，离散扩散类方案训练成本过高，亟需兼顾训练效率、生成质量、推理速度的LLM框架。
### 方法关键点
- 基于变分下界推导训练目标，由自回归编码损失+并行解码损失组成，无需蒸馏现有预训练模型，可直接从原始语料从头训练
- 编码器与解码器权重共享仅嵌入层不同，采用块自回归解码（训练块大小K=16），通过几何感知的离散辅助变量传递token间依赖，解决多token生成的一致性问题
- 后训练支持SFT与DPO对齐，推理采用二次解码：单次前向生成K个候选token，经宽松核验证规则过滤后批量接受，无需逐token校验
### 关键结果
预训练80M~3B参数模型，在通用语料、数学GSM8K、代码HumanEval、指令跟随IFEval等基准测试，对比同规模自回归LLM、离散扩散模型：1.3B参数PLM推理速度达同质量自回归模型的2.3~5.7倍，3B参数PLM在所有基准上优于1.3B所有变体，速度仍达同规模自回归模型的2.5~4.8倍，且速度-质量Pareto frontier优于所有现有非自回归/少步扩散方案。
**核心结论**：PLM的并行度随模型规模提升遵循幂律分布，模型越大，多token生成的准确率越高，推理加速收益越显著
