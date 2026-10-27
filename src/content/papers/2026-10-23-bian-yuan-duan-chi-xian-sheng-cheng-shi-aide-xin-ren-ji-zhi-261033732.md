---
title: 'Trust Mechanisms for Offline Generative AI at the Edge: A Connectivity-Regime
  Framework and an Empirical Study on a Raspberry Pi 5'
title_zh: 边缘端离线生成式AI的信任机制：连接域框架与树莓派5实证研究
authors:
- Georgios Feretzakis
- Alexandros Papaspyridis
affiliations:
- securagen.ai
arxiv_id: '2610.33732'
url: https://arxiv.org/abs/2610.33732
pdf_url: https://arxiv.org/pdf/2610.33732
published: '2026-10-23'
collected: '2026-10-27'
category: RAG
direction: 边缘离线RAG · 信任机制优化
tags:
- Edge-RAG
- Trustworthy-AI
- Offline-LLM
- Knowledge-Pack
- Edge-Intelligence
one_liner: 提出C0-C4连接域框架，在树莓派5上实测离线RAG多层信任机制的性能与开销
practical_value: '- 做离线端（如IoT导购设备、离线自助Agent）RAG系统时优先选3B级小模型，在金答案包含率与7B相当的前提下，延迟和能耗仅为7B的一半，成本收益最优

  - 边缘RAG不要盲目增加召回passage数量，实测召回3条的效果优于5条，更多上下文会分散模型注意力反而降低正确率，还会抬升延迟

  - 离线RAG的知识更新可采用签名版本化Knowledge Pack方案，校验成本仅4.5ms，比端侧重新生成嵌入快5个数量级，大幅降低端侧计算开销

  - 小模型RAG要加简单的确定性输出校验，把只有引用没有答案的异常输出转为拒答，1.5B模型的错误回答风险可从0.81降到0.46，完全不损失正确答案'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前生成式AI与LLM部署普遍依赖云端连接，但工业运维、救灾响应、离岸设施等大量IoT场景存在间歇性、受限甚至无网络的情况，离线边缘生成助理的可信性保障方法、以及信任机制在边缘硬件上的性能开销长期缺乏实测数据。现有边缘LLM研究仅关注效率优化，未将连接性作为核心设计维度，云端验证过的RAG信任机制在端侧的表现也未被量化。
### 方法关键点
- 提出C0-C4连接域框架，将连接性从云连接到物理气隙分为5个等级，对应不同的推理、更新、信任、治理方案
- 设计分层推理信任机制：检索分数门控、确定性输出校验、NLI蕴涵验证，提出带签名、版本控制的Knowledge Pack作为离线场景的知识更新渠道
- 基于树莓派5搭建完全离线RAG测试环境，测试Qwen2.5 1.5B/3B/7B 4bit量化模型，1/3/5个召回passage配置，覆盖300条SQuAD2.0问题（可答/同领域不可答/语料外三类）
### 关键结果
- 检索分数门控检测语料外知识gap的AUROC达0.97，检测同领域不可答问题仅0.68；确定性输出校验将1.5B模型的回答错误风险从0.81降至0.46，无正确答案损失
- 3B模型与7B模型的金答案包含率均为75%，但延迟仅为7B的44%、能耗仅43%；召回5条passage时正确率从75%降至52%，延迟提升63%
- 签名Knowledge Pack校验仅需4.5ms，比端侧生成嵌入快5个数量级；仅做签名哈希校验会放过6/9种更新攻击，增加版本、过期、兼容性校验可拦截所有攻击

最值得记住的一句话：所有推理侧的信任校验都无法防御合法签名的毒化知识包，离线RAG的内容信任必须在知识包签名前通过审核、溯源、对抗测试完成
