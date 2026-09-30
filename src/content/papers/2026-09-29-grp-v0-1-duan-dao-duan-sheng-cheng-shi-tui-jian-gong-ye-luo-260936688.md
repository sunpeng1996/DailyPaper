---
title: GRP v0.1 Technical Report
title_zh: GRP v0.1 端到端生成式推荐工业落地技术报告
authors:
- Wenfeng Zhuo
- Vincent Xue
- Charles Wei
- Cong Ni
- Ruiming Lu
- Jiwen Ren
- Mo Li
- Peng Yang
- Xufei Wang
- Dongheng Li
affiliations:
- Snap Inc.
arxiv_id: '2609.36688'
url: https://arxiv.org/abs/2609.36688
pdf_url: https://arxiv.org/pdf/2609.36688
published: '2026-09-29'
collected: '2026-09-30'
category: GenRec
direction: 生成式推荐 · 工业渐进式落地
tags:
- Generative Recommendation
- Semantic ID
- GRPO
- End-to-End RecSys
- Industrial Deployment
one_liner: 提出可渐进式落地的端到端生成式推荐范式GRP，统一召回排序并在短视频场景验证业务收益
practical_value: '- 落地策略可直接复用：不要全量替换现有推荐 cascade，走渐进式路径：先加为召回源平测，替换弱召回源扩容配额，再逐步绕过排序，每步可灰度可回滚，大幅降低落地风险

  - 架构设计可借鉴：生成模块和排序模块联合训练但加 stop-gradient 隔离，避免排序目标干扰生成表示，排序模块还能直接复用做 RL reward model，减少重复开发

  - RL 优化 trick 可用：生成式推荐优化业务目标时，用 mGRPO 替代原生 GRPO，加参考锚定的单边 margin 约束，避免优化时基线召回率下跌，平衡指标收益和稳定性

  - 工程优化可落地：Semantic ID 到 item 的映射异步更新解决内容新鲜度问题，KV cache + CUDA 图捕获 + 批量查询将端到端推理延迟降低
  69%，适配线上流量要求'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有端到端生成式推荐直接全量替换工业级多阶段推荐 cascade 常出现负向效果：成熟 cascade 积累了大量粒度优化（freshness 规则、eligibility 过滤、多样性控制等）纯生成器无法复现，且生成式召回排序能力不及成熟 cascade，内容库快速迭代下冻结模型的精确 item 召回率数天内骤降，直接替换也无法定位瓶颈优先级。

### 方法关键点
- 渐进式落地路径：分三阶段灰度，①作为新增召回源与现有源同口径平测定位瓶颈；②替换性能更弱的召回源逐步扩容配额；③逐步绕过早排、晚排，最终完成全量替换，每步可量化可回滚
- 架构设计：encoder-decoder 结构生成多模态 Semantic ID，联合训练多头预测（MHP）排序模块，通过 stop-gradient 隔离生成与排序梯度避免互相干扰，MHP 模块可直接复用为 RL 后训练的 reward model
- RL 优化：提出 mGRPO 算法，在 GRPO 基础上增加参考锚定的单边 margin 约束，避免优化业务目标时基线召回率下跌
- 工程优化：异步更新 Semantic ID 到 item 的映射解决内容新鲜度问题，KV cache、CUDA 图捕获、批量查询等优化将端到端推理延迟降低 69%，适配线上 latency 要求

### 关键结果
在 Snap 短视频场景线上 A/B 测试：1）GRP 作为召回源替换低性能源，带来 +0.82% 观看时长、+2.56% 分享率提升；2）mGRPO 后训练相比 SFT 模型提升 +0.45% 观看时长；3）扩大解码预算在无排序绕过时提升 +0.39% 观看时长。

### 最值得记住的一句话
端到端生成式推荐工业落地的核心不是一步替换现有系统，而是通过可量化的渐进式路径逐步迭代，平衡技术创新和业务稳定性。
