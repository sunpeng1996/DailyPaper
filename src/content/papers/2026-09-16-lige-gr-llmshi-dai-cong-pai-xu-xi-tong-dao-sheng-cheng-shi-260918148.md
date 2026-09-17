---
title: 'LIGE-GR: A Smooth Leap from Ranking to Generative Recommendation in the LLM
  Era'
title_zh: LIGE-GR：LLM时代从排序系统到生成式推荐的平滑升级框架
authors:
- Venkat Srinivas
- Chenzhang He
- Sam Woodmansee
- Shawn Lian
- Wenjie Hu
- Renjie Jiang
- Ziheng Huang
- Xinyuan Zhang
- Zhihao Zheng
- Zhuoran Yu
affiliations:
- Meta Platforms, Inc.
arxiv_id: '2609.18148'
url: https://arxiv.org/abs/2609.18148
pdf_url: https://arxiv.org/pdf/2609.18148
published: '2026-09-16'
collected: '2026-09-17'
category: GenRec
direction: 生成式推荐 · 工业级平滑迁移
tags:
- Generative Recommendation
- Listwise Optimization
- Industrial RecSys
- LLM4Rec
- Beam Search
one_liner: 在现有工业排序系统上增量升级为列表式生成推荐，无需重构全栈，Meta短视频场景验证获显著收益
practical_value: '- 存量系统升级无需重构全栈：可在现有召回/点式排序基础上，仅新增轻量上下文感知模块+列表解码层，兼容原有基建、价值模型、业务规则，迁移成本低风险小

  - 上下文感知模块轻量化设计：复用现有排序模型的中间表征，仅新增4层小参数量因果Transformer做预测，额外推理开销仅为原排序模块的10%，适配高吞吐线上场景

  - 列表价值建模可落地方案：引入用户继续浏览概率加权每个item的价值，比纯点式求和更贴合真实序列消费场景，无需改动原有价值权重逻辑

  - 解码层高可靠性设计：支持按请求粒度fallback到原有贪心排序，latency超阈值自动切回基线，上线无可用性风险，还支持开关式回滚无需重训'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业界成熟推荐系统大多基于点式独立打分排序，无法建模列表内item的上下文依赖（如用户疲劳、内容互补、多样性等），而现有生成式推荐方案大多要求重构全栈，技术风险高、组织协调成本大，难以快速落地成熟业务。

### 方法关键点
- 架构分层兼容设计：保留原有上下文无关（CF）排序模块，新增轻量上下文感知（CA）模块，输入为CF模块输出的item中间表征，用4层因果Transformer建模已选列表对当前候选的影响
- 价值模型升级：从点式独立求和升级为列表式价值，引入用户继续浏览概率加权每个item的价值，更贴合真实序列消费的曝光逻辑
- RL解码层：提出Palette解码器，基于束搜索保留多候选路径，加入时长感知的未来价值估计引导搜索，同时兼容原有贪心解码逻辑，支持一键回滚

### 关键结果
在Meta旗下Instagram Reels和Facebook Video短视频推荐场景做在线A/B测试，对比成熟工业基线：
- b=1基础配置下，Instagram Reels用户时长提升1.14%，Facebook Video时长提升0.72%，额外推理开销仅为原有CF模块的10%，端到端latency增加不到7%
- 升级为b=6时长感知配置后，Instagram Reels时长较b=1版本进一步提升0.69%

**最值得记住的一句话**：生成式推荐落地不需要一步到位重构全栈，兼容现有基建的增量式升级是工业场景更可行的路径。
