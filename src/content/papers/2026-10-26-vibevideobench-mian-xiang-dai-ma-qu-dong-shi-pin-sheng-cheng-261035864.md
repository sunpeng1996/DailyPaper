---
title: 'VibeVideoBench: Evaluating Multimodal Agents on Code-Driven Video Generation'
title_zh: VibeVideoBench：面向代码驱动视频生成的多模态Agent评测基准
authors:
- Muxi Diao
- Wenbin Xu
- Lele Yang
- Xuyang Ma
- Yuzhe Chen
- Jiankang Chen
- Kaiyu Jiang
- Changyi Liu
- Haoyu Zhang
- Hongyi Fu
affiliations:
- 北京邮电大学
- 北京大学
- 吉林大学
- Kling Team
- 中关村学院
arxiv_id: '2610.35864'
url: https://arxiv.org/abs/2610.35864
pdf_url: https://arxiv.org/pdf/2610.35864
published: '2026-10-26'
collected: '2026-10-29'
category: Eval
direction: 多模态Agent评测 · 代码驱动视频生成
tags:
- Multimodal Agent
- Benchmark
- Code Generation
- Video Generation
- LLM Evaluation
one_liner: 推出首个面向代码驱动音视频生成的多模态Agent评测基准及分层评估体系
practical_value: '- 做Agent自动生成类业务（如电商商品介绍视频、品牌短片）的效果评估时，可复用分层评测框架：先做可自动化的L1程序校验（规格、时长、合规性），再做分模态路由的L2规则校验，最后做质量打分，大幅降低人工评测成本

  - 开发带时间约束的Agent产出任务时，可优化调度策略：要求Agent优先输出完整可交付版本再迭代优化，预留至少20%的时间用于最终渲染导出，避免75%的超时无产出问题

  - 多模态内容质检可复用分模态路由方案：视觉校验交给VLM，音频/音画同步校验交给音频大模型，比单一多模态模型的评估准确率更高，适合直播切片、商品短视的批量质检'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有视频生成基准仅针对扩散模型的短无声片段，而代码驱动的视频生成可实现精准文本/数字渲染、音画同步、长时结构、可编辑，是教育科普、品牌宣传、产品演示视频的核心生产路径，但当前缺少针对通用多模态Agent完成全流程任务的评测体系，无法衡量Agent的规划、代码生成、多模态自校验、交付能力。

### 方法关键点
- 构建239个自包含任务，覆盖12个类别，支持中英双语，时长8s到15min，每个任务包含明确的规格要求、资产包、音视频政策、交付标准，无固定ground truth，仅按需求校验
- 三层分层评测体系：L1是自动程序校验（分辨率、帧率、时长、音频存在性等），L2是任务特定的基于证据的规则校验（平均每个任务54条，分模态路由给对应模型评审），L3是5个维度的质量打分
- 评测环境完全对齐实际部署：每个Agent用原生工具链，在相同沙箱、1小时时间预算下完全自主运行，不允许调用图像/视频生成模型，仅允许使用TTS工具

### 关键结果
评测9款前沿多模态Agent共2151次运行：表现最好的Claude Opus 5.5交付率100%，核心需求满足率76.3%，GPT-6 Astra紧随其后，人类偏好和多模态评审的系统级排序相关系数达0.98；75%的交付失败来自最终渲染启动过晚、运行超时，表现最好的Opus平均提前24分钟完成交付；Agent自检查次数和最终质量无相关性（ρ=-0.07），单视频模型评审和人类偏好一致性仅73%，仅系统级排序可靠。

> 最值得记住：多模态Agent做长周期交付类任务时，按时交付的可靠性和产出质量同等重要，分层+分模态路由的评估是平衡效率和准确率的最优选择
