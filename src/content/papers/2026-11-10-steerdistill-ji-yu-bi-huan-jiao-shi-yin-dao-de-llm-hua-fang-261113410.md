---
title: 'SteerDistill: Quantizing LLM Agents via Closed-Loop Teacher Steering'
title_zh: SteerDistill：基于闭环教师引导的LLM Agent量化方法
authors:
- Genming Cui
- Xiangyu Li
- Zixu Hao
- Xin Ding
- Yunxin Liu
- Ting Cao
affiliations:
- 清华大学人工智能产业研究院(AIR)
- 中国科学技术大学
arxiv_id: '2611.13410'
url: https://arxiv.org/abs/2611.13410
pdf_url: https://arxiv.org/pdf/2611.13410
published: '2026-11-10'
collected: '2026-11-11'
category: Agent
direction: Agent 低比特量化蒸馏优化
tags:
- LLM Agent
- Quantization
- Knowledge Distillation
- Low-bit Inference
- Closed-loop Guidance
one_liner: 通过闭环教师引导的量化感知蒸馏，实现低比特LLM Agent性能接近全精度，训练成本大幅降低
practical_value: '- 电商导购/客服类Agent低比特部署时，可复用闭环偏移修正逻辑：对齐全精度基线的成功轨迹定位行为偏差点，仅针对偏差点做引导修正，无需全量重训即可快速恢复量化后的任务成功率

  - 蒸馏目标设计可直接复用：偏差修正轮次用forward KL对齐带引导的学生输出，其余轮次用reverse KL对齐全精度教师输出，比单一KL目标效果提升1.5+分，推理无额外开销

  - 训练样本构造可借鉴本地验证规则：仅验证修正轮次的环境跳转是否符合成功参考，无需整条轨迹成功即可加入训练集，训练数据成本降低30%以上，收敛速度提升2倍

  - Agent训练的引导prompt推荐用结构化格式：明确标注差异点、适用条件、修正规则，比自由格式prompt的修正成功率高2个百分点以上，可直接套用模板'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM Agent多轮交互、频繁调用的特性导致推理成本居高不下，低比特量化是落地降本的核心路径，但量化后Agent易忽略任务要求或环境约束，出现与全精度基线不一致的行为偏移，任务成功率大幅下降。传统离线蒸馏缺少数值学生的失败场景样本，在线自举又很难在失败场景给出正确响应，亟需高效的量化后能力恢复方案。
### 方法关键点
- 教师引导轨迹修正：对齐全精度教师的成功轨迹，定位学生第一次行为偏移点；教师输出结构化引导prompt（含差异、适用条件、修正规则），学生基于引导重写响应，本地验证（匹配环境跳转与参考一致）通过后保留修正样本，单步最多重试4次
- 引导行为内化蒸馏：修正轮次用forward KL让无引导的学生对齐带引导的学生输出，其余轮次用reverse KL对齐全精度教师输出，推理阶段无需教师或引导prompt，无额外开销
### 关键实验
覆盖5个Agent基准（BFCL V4、τ2-Bench、WebShop、ALFWorld、Search QA）、3个主流开源模型：W4A16量化下平均得分超出最强基线QeRL 1.67~2.18分，与BF16全精度性能差距小于1分；τ2-Bench上成功率比QeRL高1.84pct，训练GPU小时数减少67%，成功轨迹平均输出token仅4.0K，接近BF16的3.9K，远低于基线的4.1K~5.2K。
### 核心结论
针对低比特Agent的行为偏移点做局部监督修正，即可用极低训练成本让量化模型接近全精度性能，无需全量重训。
