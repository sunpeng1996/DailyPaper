---
title: 'ProVe: Proposer-Verifier Decoding'
title_zh: ProVe：提案者-验证者架构的大语言模型解码加速方法
authors:
- Ziqi Jin
- Weiwen Xu
- Jiaxi Li
- Yujie Zhong
- Qi She
- Aixin Sun
affiliations:
- Nanyang Technological University
- ByteDance
arxiv_id: '2610.27815'
url: https://arxiv.org/abs/2610.27815
pdf_url: https://arxiv.org/pdf/2610.27815
published: '2026-10-19'
collected: '2026-11-03'
category: LLM
direction: 大语言模型推理 · 投机解码优化
tags:
- Speculative Decoding
- LLM Inference Acceleration
- Decoding Optimization
- Throughput Optimization
- Autoregressive Model
one_liner: 反转传统投机解码角色，大模型单步提案多token加验证，实现最高2.7倍解码吞吐量提升
practical_value: '- 业务中部署的LLM服务（如推荐文案生成、Agent对话、搜索query改写）可直接复用ProVe-lossless方案，无需额外训练小模型，即可拿到平均2.5倍的无损吞吐量提升，降低推理成本

  - 对精度要求不高的场景（如商品短文案生成、用户评论摘要），可搭配3B/7B小verifier，通过阈值调参在2.3~2.7倍吞吐量区间做速度-精度tradeoff，适配业务容忍度

  - 长文本生成场景（如商品详情页生成、多轮Agent推理）优先采用ProVe，响应长度越长速度提升越显著，结构化长任务下无损加速可达4倍

  - 可复用p_i·q_i的门控规则，比单靠模型置信度多commit 2倍以上有效token，大幅提升block解码的token利用率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统投机解码依赖小模型串行生成draft token、大模型并行验证，小模型的串行步骤拖慢了加速上限；而基于大模型自身置信度的MARS块解码方案浪费了大量有效可提交token：GSM8K数据集下提案块平均匹配AR解码的前缀长达6.6个token，但原生置信度规则仅能提交3个，存在巨大优化空间。

### 方法关键点
- 反转投机解码角色：基于MARS微调后的大模型作为proposer，单步前向生成B=16个候选token块，无需额外新增draft head
- 双验证模式适配不同场景：ProVe-lossless用proposer自身做验证，两次前向完全复现贪心AR解码结果，无精度损失；普通ProVe用更小的AR模型做verifier，单步teacher-forced前向得到每个token的置信度q_i，结合proposer的置信度p_i，采用p_i·q_i作为门控分数，提交最长满足阈值的前缀
- 成本优势显著：小验证器每周期仅需调用1次，远低于传统投机解码中小模型需要k次串行调用的成本，性价比更高

### 关键结果
在HumanEval、GSM8K等6个通用基准上，以32B Qwen2.5作为proposer：
1. ProVe-lossless平均达到2.5×AR吞吐量，精度和原生AR完全一致，性能接近专门微调的EAGLE-3 draft head，无需额外训练
2. 搭配7B开源verifier、阈值0.05时达到2.3×吞吐量，精度仅比AR低0.3个百分点；搭配3B开源verifier、阈值0.01时达到2.7×吞吐量，精度低2.6个百分点，远超同参数小模型做draft的传统投机解码（3B speculative仅1.63×吞吐量）
3. 长推理场景增益更高：BBH结构化长任务下ProVe-lossless加速可达3.98×，响应长度越长速度提升越显著

**最值得记住的一句话**：块提案的有效token利用率远高于原生置信度阈值判断的结果，多花一次小模型验证的成本，能换回远高于传统投机解码的吞吐量提升
