---
title: 'Select, Compress, Reinvest: A Controlled Study of Visual-Token Allocation
  in Long-Video MLLMs'
title_zh: 选择、压缩、再投入：长视频多模态大模型视觉Token分配受控研究
authors:
- Prakhar Khatri
affiliations:
- Independent Researcher
arxiv_id: '2609.03820'
url: https://arxiv.org/abs/2609.03820
pdf_url: https://arxiv.org/pdf/2609.03820
published: '2026-09-02'
collected: '2026-09-05'
category: Multimodal
direction: 多模态大模型 · 长视频视觉Token分配优化
tags:
- MLLM
- Long-Video Understanding
- Token Allocation
- Orthogonal Matching Pursuit
- Controlled Evaluation
one_liner: 控制变量对比长视频MLLM视觉Token分配三类策略，验证经典OMP不输定制化选择器
practical_value: '- 电商直播、商品短视频理解场景可直接复用经典OMP算法做关键帧选择，无需定制帧选择器，低成本即可达到SOTA级效果

  - 长视频处理链路可先压缩单帧视觉Token预算，将节省的配额用于提升采样帧数量，总Token不变前提下精度可提升2-3个点，性价比极高

  - 多模态策略对比必须在同一受控测试套下执行，跨论文直接对比数值偏差可达3.74点，避免错误判断策略优劣'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
长视频MLLM无法加载全量帧，帧选择、视觉Token分配常被当做预处理细节，过往方案同时修改多变量，无法归因不同策略真实收益。
### 方法关键点
固定回答模型、分辨率、prompt边界等变量，单因素对比6种免训练帧选择规则、空间压缩策略、节省Token再投入策略，覆盖3个长视频基准、2个回答模型。
### 关键结果
- 帧选择是最大影响因子：LongVideoBench小时级测试集上，8个query关联选择帧比16个均匀采样帧高6.9分；经典OMP算法在所有基准上与定制选择器效果差不超1分
- 单帧空间预算减半损失≤0.44分，将节省Token用于新增2倍压缩帧，总效果再升2-3分且总Token量不变
- 相同规则不同测试套效果差可达3.74分，必须在同一受控测试套下做策略对比
