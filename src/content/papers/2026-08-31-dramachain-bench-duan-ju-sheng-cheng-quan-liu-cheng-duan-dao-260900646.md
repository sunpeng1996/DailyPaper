---
title: 'DramaChain Bench: An End-to-End Benchmark for Short-Drama Generation'
title_zh: DramaChain Bench：短剧生成全流程端到端评测基准
authors:
- Haoyuan Shi
- Mingtao Chen
- Shuo Jiang
- Ziyan Chen
- Xuyi Sheng
- Yiming Liu
- Ying Zhang
- Miao Wang
- Jianxiang Lu
- Fanyang Lu
affiliations:
- Hunyuan, Tencent
- Beijing Film Academy
- Peking University
- Shenzhen University
arxiv_id: '2609.00646'
url: https://arxiv.org/abs/2609.00646
pdf_url: https://arxiv.org/pdf/2609.00646
published: '2026-08-31'
collected: '2026-09-03'
category: Eval
direction: 生成式内容 · 全链路自动评测
tags:
- Benchmark
- Automated Evaluation
- LLM Agent
- Multi-stage Pipeline
- Short Video Generation
one_liner: 首个覆盖短剧生产全链路的评测基准，配套专业标注体系与高一致性Agent自动评测工具
practical_value: '- 多链路生成任务评测可复用「分阶段对齐原始意图+上游缺陷归因」框架，解决单阶段评测忽略级联误差的问题

  - Agent自动评测可借鉴「多轮证据收集+预定义检查清单匹配」逻辑，可快速对齐人工标注偏好，PLCC可达0.9+量级

  - 电商短素材（广告/短剧/种草视频）自动化生产链路，可复用该基准的分维度质量校验逻辑，降低人工审核成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有短剧生成评测仅覆盖单阶段视频生成，采用人工预制输入而非真实上游链路输出，无法验证各阶段是否对齐原始脚本意图、多镜头拼接后连贯性是否达标，也无法定位上游缺陷的级联影响。
### 方法关键点
1. 覆盖脚本、分镜、关键帧、镜头视频、成片全5个生产阶段，定义5大评测轴拆解为63个叶子评估维度；
2. 配套对齐商业短剧平台标准的生产Agent、专业标注系统，5785个样本由3名专业标注员独立打分，生成1.7万+有效分数、25.6万可追溯归因记录；
3. 实现Agentic Judge自动评测，多轮收集证据后对照检查清单打分。
### 关键结果
Agent自动评测与人工标注的模型排序一致性PLCC达0.918，可零标注成本完成新模型评测；同时验证上游缺陷会沿链路级联放大，成片质量不由单阶段视频生成效果单独决定。
