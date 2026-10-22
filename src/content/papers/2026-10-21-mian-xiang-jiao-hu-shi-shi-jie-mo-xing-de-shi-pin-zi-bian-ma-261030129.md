---
title: Rethinking Video Autoencoders for Interactive World Models
title_zh: 面向交互式世界模型的视频自编码器优化研究
authors:
- Adrien Ramanana Rahary
- Yutong Bai
- Nicolas Dufour
- Patrick Pérez
- David Picard
affiliations:
- Kyutai
- LIGM (ENPC, IP Paris, CNRS, UGE)
- UC Berkeley
arxiv_id: '2610.30129'
url: https://arxiv.org/abs/2610.30129
pdf_url: https://arxiv.org/pdf/2610.30129
published: '2026-10-21'
collected: '2026-10-22'
category: Agent
direction: 交互式世界模型 · 视频自编码器优化
tags:
- World Model
- Video Autoencoder
- Diffusion Decoder
- Latent Compression
- Interactive Agent
one_liner: 提出覆盖多时空压缩比的CADRE扩散自编码器家族，优化交互式世界模型的时延-质量权衡
practical_value: '- 做AR/VR电商导购、直播间交互式虚拟人等静态机位场景时，可提升自编码器时间压缩比降低时延，仅需保留较小空间压缩比避免丢失商品细节；移动机位AR逛街场景则相反，优先压缩空间维度

  - 低时延视频生成场景可复用CADRE的单阶段自蒸馏少步扩散解码器，无需二次蒸馏即可实现1-2步解码，强压缩下FVD较感知回归解码器降低1.4~2.5倍，时延相当

  - 世界模型架构设计时，优先将时间压缩模块下沉到自编码器层，避免在上游世界模型做时序patch压缩，相同token量下可获得更优的视频清晰度和动作跟随性'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有交互式世界模型大多复用文生视频的预训练自编码器，这类自编码器针对离线生成设计，时间压缩比过高（8倍压缩会带来400ms以上动作时延，超过人类可感知的230ms阈值），且不开源训练数据/代码无法重训调整压缩比，完全无法适配交互场景的低时延需求。

### 方法关键点
- 提出CADRE自编码器家族，仅调整瓶颈层3D卷积的步长即可覆盖7种时空压缩比，其余权重全部共享，大幅降低多压缩比场景的训练成本
- 解码器采用因果扩散结构，通过单阶段渐进自蒸馏实现1-2步快速解码，无需对抗损失或二次蒸馏流程，推理速度与感知回归解码器相当
- 量化明确时间/空间压缩比对世界模型的算力成本、动作时延、生成质量的影响关系，解耦「压缩多少」和「在哪里压缩」两个核心问题

### 关键结果
在机器人操作、人手操作、自动驾驶、室内导航4个场景测试，对比Wan 2.2、Cosmos、LTX-2等5个SOTA自编码器：
1. CADRE覆盖90%以上的时延-质量帕累托前沿，单H100上世界模型可跑20fps，动作时延低于230ms人类感知阈值
2. 强压缩下扩散解码器比感知回归解码器FVD低1.4~2.5倍，动作跟随性（ARR）基本一致
3. 自编码器侧做时间压缩比世界模型侧做时序patch压缩的FVD最高低28点，动作跟随性仅在8倍压缩时出现明显下降

### 最值得记住的一句话
静态摄像头场景优先做时间压缩，移动摄像头场景优先做空间压缩，粗空间token对动作/运动质量的伤害远大于对静态画质的伤害
