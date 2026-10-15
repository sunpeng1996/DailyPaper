---
title: 'CommerceGen-Studio: An End-to-End Framework for Commercial-Grade Main-Image
  Generation'
title_zh: CommerceGen-Studio：商用级电商SKU主图生成端到端框架
authors:
- Xiaoli Xu
- Zhengtao Wu
- Zhengze Xu
- Tao Liu
- Yongchao Du
- Zuan Gao
- Xingjian Wang
- Hao Yan
- Mengting Chen
- Wei Li
affiliations:
- Alibaba Group
- Taobao App
- AI-Native Applications Group
arxiv_id: '2610.20603'
url: https://arxiv.org/abs/2610.20603
pdf_url: https://arxiv.org/pdf/2610.20603
published: '2026-10-14'
collected: '2026-10-15'
category: Multimodal
direction: 电商多模态主图生成 · 大规模商用落地
tags:
- E-commerce Content Generation
- Diffusion Transformer
- Agent Pipeline
- RL for Diffusion
- Commercial Deployment
- Generation Benchmark
one_liner: 提出端到端商用级电商SKU主图生成框架，已落地千万级日产能，性能比肩头部闭源模型
practical_value: '- 可复用PERL-Agent闭环框架处理电商多源异构信息提取（如SKU卖点、评论卖点挖掘），采用无参考评分 rubric +
  最差维度优先优化策略，避免单点错误导致下游不可用，无需按品类逐个写规则

  - 扩散模型落地业务可参考RDR渐进式训练范式：先RL对齐人类偏好，再蒸馏压缩采样步数降低延迟，最后二次RL补回蒸馏损失的细节（如文字、商标精度），平衡生成质量和推理速度，适配大流量生产环境

  - 多阶段任务优化可参考LTO双域随机更新策略，每次随机选择文本/图像reward域做反向传播，避免不同域的梯度冲突，无需复杂权重调参即可同时对齐上游规划和下游生成的一致性

  - 生成类业务上线前可复用CommerceGen-Bench的难例构造思路，优先覆盖长尾品类、小字/小logo、复杂结构等高风险case，确保评测结果和线上表现对齐'
score: 9
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
电商搜索推荐页对SKU粒度主图需求强烈，但商家大多仅上传白底商品图，直接投放会显著降低CTR；通用文生图模型无法满足电商场景卖点合规、主体保真、商标一致、文字零错误的强约束，级联式系统误差累积严重，亟需端到端商用级生成方案。

### 方法关键点
- 三阶段全链路pipeline：PERL-Agent（VLM+3个LLM角色，迭代提取合规卖点列表，按6维无参考评分优化最差维度，全品类适配）→ Layout Thinker（双域优化VLM，将卖点转换为可执行布局caption）→ SKU-DiT（多条件Diffusion Transformer，同时输入白底图、logo、布局caption生成主图）
- 训练策略：RDR渐进式训练，先RL对齐偏好（分复杂布局、主体保真两个专家教师蒸馏融合），再动态反向模拟蒸馏将采样步数压到8步，最后二次RL恢复蒸馏损失的文字、logo精度；LTO双域优化，每次随机选文本/图像reward域更新，避免梯度冲突。

### 关键结果
- 自建CommerceGen-Bench，覆盖全品类400个线上难例，评测维度含主体保真、指令遵循、商品融合等5项。
- 无prompt增强时，6B参数的SKU-DiT整体得分9.42/10，超过所有开源基线，仅落后3个头部闭源模型，其中指令遵循、商品融合两个上线核心指标超过部分闭源模型。
- 已落地淘宝生产环境，日产能千万级，单图延迟仅数秒。

最值得记住的一句话：业务落地的生成系统不能孤立优化生成模型，必须从上游信息提取到下游生成全链路联合优化，同时在训练中平衡质量、延迟、合规三个核心约束。
