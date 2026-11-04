---
title: 'FlagRot: Selective Rotation for Low-Bit KV Caches'
title_zh: FlagRot：面向低比特KV缓存的选择性旋转优化方法
authors:
- Kunming Shao
- Xijie Huang
- Jierun Chen
- Jiaqi Shao
- Yanli Wang
- Jiangnan Yu
- Qiwei Li
- Wei Zhang
- Kwang-Ting Cheng
- Chi Ying Tsui
affiliations:
- The Hong Kong University of Science and Technology
- Meta
- Sun Yat-sen University
- Wuhan University
arxiv_id: '2611.03992'
url: https://arxiv.org/abs/2611.03992
pdf_url: https://arxiv.org/pdf/2611.03992
published: '2026-11-02'
collected: '2026-11-04'
category: LLM
direction: LLM推理优化 · KV缓存量化
tags:
- KV cache
- quantization
- LLM inference
- long context
- vLLM
one_liner: 针对低比特KV缓存固定旋转的精度损失问题，提出按需选择旋转的轻量化方案，不增内存提升长上下文表现
practical_value: '- 可直接将FlagRot作为vLLM插件集成到现有长上下文LLM服务中，2.5比特KV缓存下可提升128k上下文RULER得分2.9点、LongBench最高提1.94点，无需改模型即可优化电商客服Agent、长会话推荐的推理精度

  - 自适应变换的思路可复用：对Embedding量化、向量检索的向量压缩场景，可按子块统计特性选择最优预变换，选择位存入现有量化参数的符号位，不额外占用内存即可降低压缩误差

  - 量化轴与决策粒度的匹配逻辑可迁移：per-channel量化场景固定每头变换策略，完全无写入开销；per-token量化场景按样本决策换更高精度，可平衡推荐系统特征量化、召回向量压缩的精度与性能

  - 2.5比特KV缓存可将单卡32k上下文并发数提升到BF16的6倍，吞吐量达3倍，可大幅降低长会话推荐、Agent服务的GPU部署成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
长上下文LLM推理的核心瓶颈是KV缓存内存占用，2比特量化可将KV缓存体积缩小6倍，但常规固定旋转的量化优化存在明显局限：旋转仅对尖峰分布的key友好，会让平坦分布的key产生新峰值反而增大量化误差，同一key内两种子块共存，全局固定旋转会残留大量精度损失，限制低比特KV缓存的落地。
### 方法关键点
- 以32通道为子块单位，对每个子块分别测试原始状态、Hadamard旋转两种方案，选择校准后注意力误差更小的方式存储，决策位存入量化scale的符号位，不额外占用内存
- 读取时不反向旋转key，而是将query旋转到对应基上，一次旋转可共享给所有缓存token，开销极低
- 适配不同量化轴：per-channel量化（如KIVI）可固定每头的旋转策略，完全无写入开销；per-token量化按key决策，精度收益更高
- 支持INT2/INT3/INT4/FP4等多种量化精度，可直接作为vLLM插件集成，无需修改模型权重
### 关键实验
- 校准用WikiText-2数据集，在12款3B-27B开源LLM、LongBench、RULER、Agent任务τ2-bench、SWE-bench上验证
- 对比基线包括KIVI、RotateKV、RTN量化等主流方案
- 核心结果：2.5比特KV缓存下，12模型平均KL散度从KIVI的18.7×10⁻³降至12.4×10⁻³，9款模型优于RotateKV；128k上下文RULER得分提升2.9点，LongBench最高提升1.94点，32k上下文下吞吐量达BF16的3倍；4比特量化下KL散度相对RTN降低13%-89%，Agent任务精度接近BF16水平
### 核心结论
低比特量化的特征变换无需全局固定，按子块统计特性自适应选择最优变换，可在不增加内存开销的前提下大幅提升精度。
