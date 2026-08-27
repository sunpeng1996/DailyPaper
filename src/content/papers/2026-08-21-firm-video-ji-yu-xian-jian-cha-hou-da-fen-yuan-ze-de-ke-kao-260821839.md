---
title: 'FIRM-Video: Check Before You Score for Reliable Text-to-Video Reward Modeling'
title_zh: FIRM-Video：基于先检查后打分原则的可靠文生视频奖励建模
authors:
- Peiyuan Zhang
- Xiangyu Zhao
- Hongbo Liu
- Xiaoxing Hu
- Mingxin Liu
- Shuran Ma
- Yunhang Shen
- Jian Hu
- Haihan Gao
- Haoyu Cao
affiliations:
- Shanghai Jiao Tong University
- Tencent Youtu Lab
- Tongji University
arxiv_id: '2608.21839'
url: https://arxiv.org/abs/2608.21839
pdf_url: https://arxiv.org/pdf/2608.21839
published: '2026-08-21'
collected: '2026-08-27'
category: Multimodal
direction: 多模态奖励建模 · 文生视频评估对齐
tags:
- Reward Modeling
- Text-to-Video
- VLM
- Checklist-driven
- Best-of-N Sampling
one_liner: 提出check-before-score的清单驱动文生视频奖励建模框架，产出对齐人类判断的高效8B端侧奖励模型
practical_value: '- 做电商AI生成短视频、商品素材等生成内容的质量评估时，可复用分维度检查清单思路，拆解为指令匹配、常识合规、视觉质量三类可验证原子问题，避免整体打分的主观偏差

  - 训练生产可用的轻量奖励模型时，可复用「复杂多阶段pipeline离线生成高质量标注→蒸馏到小模型」的范式，兼顾标注质量和推理效率，适配best-of-N选路等低延迟场景

  - 电商短视频生成的RLHF对齐优化中，可直接复用三个维度的评分体系，分别优化文案匹配度、内容合理性、视觉清晰度，提升用户对AI生成商品内容的接受度'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有文生视频奖励模型多采用固定规则整体打分或开放式推理，存在检查不全面、理由不可信、归因纠缠三大问题，无法兼顾评估准确性与推理效率，严重制约文生视频生成效果与人类偏好的对齐。
### 方法关键点
- 遵循`check-before-score`核心原则，拆解为**指令遵循（IF）、世界一致性（WC）、感知质量（PQ）**三个独立评估维度，每个维度构建专属可验证检查清单，逐个验证后聚合得分，彻底避免跨维度归因冲突；
- 各维度差异化设计：IF将prompt拆解为带重要性权重的原子要求，加权计算满意度；WC先从视频中接地实体/动作再生成合规检查项，仅用prompt区分刻意奇幻内容与常识错误；PQ用通用视觉缺陷清单检查，仅用prompt区分艺术风格与渲染错误；
- 离线用复杂多阶段大模型pipeline生成88K条高质量维度级标注（FIRM-Video-90K），蒸馏到8B参数轻量VLM，推理时单步前向即可输出评分与解释，兼顾效果与 latency。
### 关键结果
- 构建专家标注基准FIRM-Video-Bench，含250条视频750条维度级标注；
- 基于Qwen3-VL-8B微调的模型在Bench上整体MAE低至0.78，优于GPT-5、Gemini-3.1-Pro等闭源模型；
- Best-of-8采样时，在3个主流文生视频生成器上VBench总得分比最优竞品高0.27~1.01，语义匹配得分高1.24~2.11。
> 最值得记住的一句话：将复杂评估任务拆解为可独立验证的原子检查项再加权聚合，是兼顾评估可靠性、可解释性和推理效率的通用路径。
