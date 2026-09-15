---
title: 'Look Before You Leap: Factual Decoding with Internal Attribution Signals'
title_zh: 基于内部归因信号的LLM事实性解码框架DESCAPE
authors:
- Hayeong Ryu
- JungMin Yun
- Byeonggeuk Lim
- Sunhee Jo
- YoungBin Kim
affiliations:
- Chung-Ang University Department of Artificial Intelligence
- Chung-Ang University Graduate School of Advanced Imaging Sciences, Multimedia and
  Film
arxiv_id: '2609.15745'
url: https://arxiv.org/abs/2609.15745
pdf_url: https://arxiv.org/pdf/2609.15745
published: '2026-09-14'
collected: '2026-09-15'
category: LLM
direction: LLM事实性解码 · 解码时干预
tags:
- Hallucination Mitigation
- Decoding Strategy
- Internal Probe
- Factual Generation
- Inference Optimization
one_liner: 通过LLM内部事实敏感层归因信号实现解码时幻觉干预，仅引入1.10×延迟开销
practical_value: '- 电商/广告场景下的商品详情生成、客服QA等高事实要求场景，可直接复用DESCAPE的轻量探针+解码评分逻辑，无需修改基座参数或外挂校验LLM，仅1.1倍延迟开销即可提升输出事实性

  - 可复用滑动窗口MLP消融方法定位业务微调后LLM的事实敏感层，针对场景定制的模型可快速适配该解码框架，无需重新设计干预逻辑

  - 探针训练采用模型内部消融信号做监督，无需人工标注事实标签，业务场景下可快速基于自有指令数据微调探针，适配垂直领域事实性要求'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有RAG、SFT、RLHF等幻觉缓解方案各有局限：RAG依赖检索质量且延迟高，SFT/RLHF训练成本高易出现灾难性遗忘，且自回归生成的早期事实错误会滚雪球式放大，事后修正或权重级干预都无法提前阻断，亟需低开销的解码时干预方案。

### 方法关键点
- 用滑动窗口MLP消融定位LLM内部的事实敏感层跨度：该层输出的归因信号对实体、数值等事实类token响应显著升高，对幻觉token会出现异常尖峰，可作为高风险生成的前置信号
- 训练轻量3层MLP探针，以消融得到的真实归因信号为监督，仅需单前向传播即可近似得到每个候选token的事实归因得分，无需额外的多遍前向计算
- 解码时将探针输出融入候选评分：对归因得分超过风险阈值的候选加惩罚，对落在稳定事实区间的候选加奖励，提前阻断高风险生成路径，抑制错误滚雪球

### 关键结果
在TruthfulQA、FreshQA、FACTSCORE等5个事实性基准上测试3款开源LLM（Llama-3.1-8B、Mistral-7B、Qwen2.5-7B），Llama-3.1上TruthfulQA的T*I指标达48.5%，比基线最高提升4.1个百分点，FACTSCORE达67.2，大幅领先所有基线；整体仅引入1.10×的延迟开销，远低于Self-Refine（7.24×）等方案。

**最值得记住的一句话**：LLM中间层本身就蕴含独立于输出分布的事实性信号，无需外挂模块即可实现低成本的解码时幻觉干预。
