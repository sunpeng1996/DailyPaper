---
title: Rethinking the Generation Order of Block Diffusion Language Models
title_zh: 块扩散语言模型生成顺序优化与并行自回归解码方法
authors:
- Kai Syun Hou
- James Kwok
affiliations:
- The Hong Kong University of Science and Technology
arxiv_id: '2607.24306'
url: https://arxiv.org/abs/2607.24306
pdf_url: https://arxiv.org/pdf/2607.24306
published: '2026-07-27'
collected: '2026-07-28'
category: LLM
direction: 扩散LLM 采样策略优化
tags:
- Diffusion LLM
- Block Diffusion
- Decoding Strategy
- Parallel Generation
- Autoregressive Sampling
one_liner: 提出无需训练的PARD采样策略，适配块扩散LLM的自回归偏好，兼顾解码质量与并行效率
practical_value: '- 业务中使用块扩散类LLM生成电商文案、商品标题、搜索query时，可直接替换原有采样器为PARD，无需修改训练逻辑，就能在质量损失小于0.6个点的前提下获得1.3~3.6倍的吞吐量提升，降低推理成本

  - 对于从AR预训练LLM微调得到的扩散模型，优先采用左到右约束的采样策略，比任意顺序采样效果更优，无需投入成本调优复杂的任意顺序采样规则

  - 做LLM生成服务优化时，PARD的前缀约束逻辑可与KV cache复用能力结合，进一步提升长文本生成效率，适合批量文案生成、多轮Agent回复等业务场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
现有扩散语言模型（DLM）的采样方法大多针对早期全序列掩码扩散模型（MDM）设计，近期性能更优的块扩散语言模型（BDLM）多从预训练AR LLM微调而来，现有任意顺序采样策略未匹配BDLM天生的自回归偏好，无法平衡生成质量与解码效率，落地价值受限。
## 方法关键点
- 先通过实验与理论分析证明：BDLM训练过程中更常接触左到右的掩码上下文，相比MDM对AR解码的适配性更强，纯AR采样在BDLM上效果超过所有任意顺序采样器。
- 提出无训练开销的并行自回归解码（PARD）：保留AR左到右前缀约束，每步从左到右扫描掩码位置，将满足置信度/边际/熵阈值的最长连续前缀同时解掩码，阈值不满足时回退到解最左掩码位。
- 兼容现有任意顺序采样的打分规则，同时支持块间KV cache复用，无需修改模型结构或训练流程，可直接接入现有BDLM。
## 关键实验
在3款主流BDLM（Fast-dLLM v2 7B、SDAR 8B、LLaDA2.1-Mini 16B）、6类基准任务（代码生成、数学推理、指令遵循等）上测试，对比AR采样、Confidence、Margin、Entropy、KLASS等10余种baseline：
- PARD比所有现有并行采样器平均准确率高2.4~4.4个百分点，代码生成类任务提升更明显。
- 相比纯AR解码，PARD仅损失0~0.6个百分点准确率，吞吐量提升1.3~3.6倍，最高可达3.64倍。
- 固定左到右多token生成的静态策略效果下降明显，PARD的自适应阈值筛选是保证质量的核心。
## 核心结论
从AR预训练模型改来的块扩散LLM，左到右约束的并行采样比任意顺序采样的质量-效率tradeoff更优
