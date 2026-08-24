---
title: Personalized Privacy Control in LLMs via Attention Head Intervention
title_zh: 基于注意力头干预的大模型个性化隐私控制方法
authors:
- Junseok Kim
- Nakyeong Yang
- Kyomin Jung
affiliations:
- IPAI, Seoul National University
- Max Planck Institute for Software Systems
arxiv_id: '2608.21209'
url: https://arxiv.org/abs/2608.21209
pdf_url: https://arxiv.org/pdf/2608.21209
published: '2026-08-21'
collected: '2026-08-24'
category: LLM
direction: 大模型隐私控制 · 推理时干预
tags:
- LLM Privacy
- Attention Head Intervention
- Inference-time Steering
- Personalized Policy
- Privacy Benchmark
one_liner: 提出推理时注意力头干预方法REPAIR与个性化隐私基准P3Bench，大幅提升大模型隐私政策遵从度
practical_value: '- 开发电商个人助理、用户专属Agent等需要访问敏感数据的应用时，不要完全依赖prompt注入隐私规则，7B级模型政策忽略率可达50%+，易造成用户地址、健康信息等敏感数据泄露

  - 可复用REPAIR的无微调干预方案：通过线性探针筛选控制隐私决策的关键注意力头，针对披露/拒绝场景分别构造干预向量，仅在推理时执行干预，尤其适合端侧部署的轻量Agent场景

  - 做LLM应用隐私合规评测时，可复用P3Bench的双指标范式，同时评估过度泄露、过度拒绝两类错误，比单一准确率更贴合实际业务的合规风险

  - 注意力头干预的思路可迁移到推荐系统硬规则对齐场景，比如用户明确要求不推送某类内容的规则，比prompt注入更稳定可靠'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Agent化LLM广泛调用用户个人数据完成预定任务，现有上下文隐私规则多为全局固定范式，但不同用户对同一类信息的披露容忍度差异极大；实测直接通过prompt注入用户个性化隐私政策的方案失效严重，Qwen2.5-7B平均政策忽略率达51.25%，Gemma3-4B甚至高达74.28%，存在严重的过度泄露或过度拒绝问题，无法满足个性化隐私要求。
### 方法关键点
- 构造P3Bench个性化隐私评测基准，基于现有上下文隐私数据集扩展4类典型用户隐私策略（最高隐私、仅开放联系方式、仅开放健康信息、仅开放偏好信息），覆盖3536个测试用例
- 推理时无微调干预方法REPAIR：首先用线性探针从所有注意力头中筛选出对隐私决策敏感度最高的Top-k头；针对不同披露状态构造差异化干预向量：拒绝场景直接用真值校准的激活值替换头输出，允许披露场景用披露/拒绝激活的归一化差向量做方向引导，避免覆盖输入相关的业务信息；推理时先通过多探头多数投票预测当前请求的披露状态，再执行对应干预
### 关键实验
在Qwen2.5 3B/7B、Gemma3 4B三个开源模型上，对比直接prompt、CoT、CAST、AdaSteer等基线，REPAIR在最高隐私策略下将Qwen2.5-3B的综合隐私错误率（PED）降低90.5%，Gemma3-4B降低67.8%，同时降低过度拒绝和过度泄露两类错误；跨随机组合的用户隐私策略下仍保持稳定效果，且用全局校准的探针也能达到接近策略专属校准的性能。

> 最值得记住：大模型默认的披露偏好极难通过prompt修改，对涉及用户敏感数据的Agent应用，推理时注意力头干预的规则对齐效率和可靠性远高于prompt工程
