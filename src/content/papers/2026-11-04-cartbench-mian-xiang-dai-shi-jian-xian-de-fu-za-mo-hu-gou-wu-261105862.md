---
title: 'CARTBench: Rubric-Based Evaluation of Shopping Advice for Complex and Ambiguous
  Requests with Timelines'
title_zh: CARTBench：面向带时间线的复杂模糊购物请求的评估基准
authors:
- Yuqin Dai
- Zhanwei Zhang
- Honghui Yang
- Zhouheng Yao
- Yueqi Zhang
- Jingyu He
- Chaoyang Shi
- Fanding Wei
- Boyuan Pan
- Kai Xu
affiliations:
- Zhejiang University
- Xiaohongshu Inc.
- Tsinghua University
- Shanghai Jiao Tong University
arxiv_id: '2611.05862'
url: https://arxiv.org/abs/2611.05862
pdf_url: https://arxiv.org/pdf/2611.05862
published: '2026-11-04'
collected: '2026-11-05'
category: Eval
direction: 电商购物Agent · 评估基准构建
tags:
- LLM Agent
- E-commerce Recommendation
- Evaluation Benchmark
- Conversational Recommendation
- Rubric-based Evaluation
one_liner: 构建带时间线的复杂模糊购物请求评估基准，测试10款主流LLM并识别理解-执行差距
practical_value: '- 可直接复用论文提炼的4条Ideal Response Principles优化购物Agent的prompt，无需从零梳理回复规范，快速提升生成回复的合规性与实用性

  - 搭建自研购物Agent评估体系时，可复用Core/Excellence/Safety三层rubric设计思路，结合证据绑定的打分逻辑，降低评估偏差、减少人工标注成本

  - 优化对话式购物推荐效果时，可针对性规避三个高频失败点：无依据的产品宣称、不合理的适用性推断、过早消解未知需求，快速提升用户满意度

  - 需做LLM选型对比时，可直接使用CARTBench的169个低测试成本用例（单模型评估成本低于24美元），快速完成不同模型在电商购物场景的效果排序'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM购物助手已广泛支持多轮对话推荐，但针对需求复杂模糊、带时间维度变化（如需求过期、变更）的场景，既缺乏公开的真实商业标注数据，也没有统一可落地的评估标准。现有购物基准要么未纳入时间线维度，无法识别回复是否匹配已过期的需求，要么不支持对条件性回答的合理判定，无法区分蒙对的结果和有依据的推荐，难以衡量购物Agent的真实服务能力。
### 方法关键点
- 数据层：从真实商业场景分层采样17个零售领域的169个CART（复杂模糊带时间线）场景，配套1603条真实商品记录，完整保留带时间戳的对话上下文、过期/未确认需求信息
- 评估框架：从成功订单的优质回复中提炼4条通用Ideal Response Principles，再基于原则为每个case定制分层评估规则：Core（基础合规要求）、Excellence（高质量决策帮助）、Safety（风险管控），共含1328条专家标注规则
- 评估流程：提出Principle-Guided CART Prompting引导模型生成推荐，评估时规则对模型不可见，采用证据绑定的自动打分加专家校验的方式完成评估，一致性达99.69%
### 关键实验
测试覆盖7款主流商用API模型（含GPT-6.1-Sol、Claude-Opus-5）和3款35B+参数开源Qwen3.5模型：3款模型Core通过率超90%，但所有模型Excellence通过率最高不足40%，明确存在理解-执行鸿沟；高频Core失败点中，无依据产品宣称占30.8%、不合理适用性推断占22.1%；即使通过所有需求和证据校验的回复，仍有13%存在计划可行性问题。
### 核心结论
购物Agent仅做到需求理解正确、产品信息准确还不够，必须基于已知信息给出可落地的决策支持，不能对未知信息做无依据假设
