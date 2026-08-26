---
title: Is Discrete Difficulty Sufficient? Leveraging Continuous Difficulty for Efficient
  Self-Consistency in LLMs
title_zh: 利用连续难度信号实现LLM高效自一致性推理
authors:
- Sihyeong Yeom
- Geon Park
- Geunyeong Jeong
- Taewoong Yoon
- Jaewook Lee
- Harksoo Kim
affiliations:
- Konkuk University
- DATUMO INC.
arxiv_id: '2608.24590'
url: https://arxiv.org/abs/2608.24590
pdf_url: https://arxiv.org/pdf/2608.24590
published: '2026-08-25'
collected: '2026-08-26'
category: Reasoning
direction: LLM推理优化 · 自一致性解码
tags:
- Self-Consistency
- Inference Efficiency
- Continuous Difficulty
- Entropy Probe
- Test-Time Scaling
one_liner: 以输出熵为连续难度信号，通过轻量探针动态调整自一致性采样路径，最高节省76%推理token
practical_value: '- Agent复杂推理（如电商客服多轮逻辑判断、商品搭配推理）场景可复用连续难度估计思路，不用给所有query分配固定推理步数，用熵探针动态调整资源，大幅降低token成本

  - 生成式推荐的多候选校验环节（如个性化文案生成、多品排序投票）可替换固定次数自一致性采样为FSC的动态预算机制，效果持平前提下显著降低推理延迟

  - 轻量线性探针仅依赖LLM最后一个token的embedding输出，无需修改模型结构，可快速接入开源LLM推理链路，低成本实现推理资源的动态调度'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
Self-Consistency（SC）是提升LLM复杂推理效果的核心解码策略，通过多路径采样+多数投票输出答案，但固定采样次数的模式存在严重资源浪费：简单query仅需1-2条路径即可收敛，仅高难度query需要多路径探索。现有基于离散难度分级（简单/困难）的优化方案无法捕捉同一分级内的细粒度难度差异，依然存在资源错配问题，亟需更精准的难度度量方法平衡推理效果与成本。
### 方法关键点
- 选择LLM输出答案分布的熵作为连续难度信号，验证熵值与模型不确定性、问题难度正相关，替代传统离散分级机制
- 训练轻量线性探针：用MATH数据集7500条样本，每条生成40条推理路径计算真实熵作为标签，输入为LLM处理query后的最后一个token embedding，仅用MSE loss优化，无额外非线性层
- 动态采样逻辑：将预测熵clip到[0, log2N]区间（N为最大采样数，默认40），归一化后映射为采样路径数，低熵简单query最少分配1条路径，高熵难query最多分配N条路径
### 关键结果
在MATH500、AMC23、AIME系列、GPQA-D、MMLU-Pro等多数据集上，对比SC、AC、ESC、DSC等基线，覆盖Qwen2.5 3B/7B/14B、Gemma-3-4B等多款模型：FSC保持与SC持平的推理准确率，最高降低76.7%的token消耗，效果优于所有离散难度优化的基线，跨领域泛化性强，OOD场景下表现稳定。
最值得记住的一句话：基于模型内部输出熵的连续难度调度是几乎无额外 overhead 的Test-Time Scaling方案，可快速落地到各类LLM推理场景。
