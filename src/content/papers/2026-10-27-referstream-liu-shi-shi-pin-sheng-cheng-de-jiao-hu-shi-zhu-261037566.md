---
title: 'ReferStream: Interactive Subject Injection for Streaming Video Generation'
title_zh: ReferStream：流式视频生成的交互式主体注入框架
authors:
- Shuolin Xu
- Guanyuan Li
- Boyu Li
- Kelu Yao
- Xiaogang Xu
- Hongchuan Yu
- Shuicheng Yan
- Xiaobin Hu
affiliations:
- Bournemouth University
- National University of Singapore
- Zhejiang University
- HKUST
- Zhejiang Lab
arxiv_id: '2610.37566'
url: https://arxiv.org/abs/2610.37566
pdf_url: https://arxiv.org/pdf/2610.37566
published: '2026-10-27'
collected: '2026-10-29'
category: Multimodal
direction: 多模态生成 · 流式视频主体注入
tags:
- Streaming Video Generation
- Reference Injection
- Cache Management
- Training-free
- Multimodal Generation
- Benchmark
one_liner: 提出无需额外训练的流式视频生成交互式主体注入框架及配套基准 性能优于现有基线
practical_value: '- 流式生成场景的 transient cache 注入+恢复方案可直接复用，避免新输入干扰已生成上下文，适合电商实时个性化短视频、直播内容生成场景

  - 无额外训练的新特征融合思路：将新参考隐向量嵌入当前场景隐向量的目标区域，可迁移至多模态生成式推荐的实时个性化商品主体注入

  - 按事件时序调度的多维度评测方法，可借鉴用于流式推荐、实时互动内容生成系统的效果评估'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
流式视频生成过程中动态插入新视觉参考主体时，现有方案存在两大痛点：独立编码参考特征缺乏上下文融合指导，持久存储参考特征会干扰已建立的场景上下文，且大多需要重训模型或修改已输出帧。
### 方法关键点
1. 提出训练免的ReferStream框架，融合基于当前场景的参考构建与瞬时缓存注入能力；
2. Joint Latent模块将参考隐向量嵌入最新场景隐向量的目标区域，实现上下文感知的参考特征提取；
3. Cache Restoration模块用上述特征约束注入块，恢复被覆盖的全局缓存条目同时保留新生成历史，无需重训生成器或修改已输出帧；
4. 配套发布ReferStream Bench基准，覆盖单/多镜头生成，标注主体出现时序，支持按事件调度评测。
### 关键结果
在ReferStream Bench上，文本一致性、主体相似度、计数准确率指标均优于所有对比基线，包括提前拿到全部参考的离线方法。
