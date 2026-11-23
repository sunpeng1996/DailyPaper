---
title: 'Silent Arbitration: How Large Language Models Resolve Co-Authoritative Conflicting
  Instructions'
title_zh: 静默仲裁：大语言模型如何解决同等权威的冲突指令
authors:
- Sihyeon Lee
- Jiwoo Kum
- Jihun Song
- Chanwoo Kim
- Chanjun Park
affiliations:
- Soongsil University
arxiv_id: '2611.27444'
url: https://arxiv.org/abs/2611.27444
pdf_url: https://arxiv.org/pdf/2611.27444
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: LLM指令遵循 · 冲突人设处理
tags:
- Instruction Following
- Persona Prompting
- Conflict Resolution
- LLM Behavior
- Prompt Engineering
one_liner: 揭示LLM面对同等权威的冲突人设时会静默仲裁，且存在系统性立场偏向
practical_value: '- 搭建电商客服、导购等业务Agent时，避免同时赋予同等权威的对立人设（如既要极致优惠又要保毛利），需提前明确人设优先级规则，防止模型静默偏向某一方导致业务损失

  - 涉及多目标冲突的prompt设计优先采用融合特质的表述，而非并列多个独立角色，可降低输出的立场波动，提升业务可控性

  - Agent的指令遵循评估需补充冲突场景校验项，除输出质量外，还要验证模型是否主动披露冲突、仲裁策略是否符合业务预设，避免隐式偏向引发客诉'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM作为通用Agent被广泛赋予角色、价值观、沟通风格等高层指令，现实场景中这类指令常存在无预设优先级的同等权威冲突，现有研究多关注有明确层级的指令冲突，对同等权威的人设冲突下的LLM行为缺乏系统性探索，可能导致用户在不知情的情况下得到有偏向的输出，引发业务风险。
### 方法关键点
- 构造8类基于公开数据集的对立人设对（如买家/卖家、风险偏好/风险厌恶、支持性反馈/批判性反馈等），每类配20个平衡的任务探针+1个直接兼容性问题
- 设置3种同等权威冲突的prompt framing（并列连词、双角色声明、特质融合），对比单人设、无人设基线，覆盖gemma-3-12b、llama-3.1-8b等5款主流中小规模LLM
- 从冲突感知、仲裁策略、立场偏向三个维度标注输出，采用跨模型族的LLM-as-judge做标注，补充无标注器的表面特征校验结果
### 关键结果
模型在直接询问时72%能识别冲突，但普通任务响应中仅22%主动披露冲突，存在显著披露gap；45%的冲突场景输出直接偏向某一人设，35%的表面妥协类输出仍存在隐性立场偏向；不同prompt framing对仲裁形式的影响是普通paraphrase的8.8倍，双角色声明更易输出分立场的内容，特质融合更易出现单方偏向。
### 核心结论
同等权威的冲突指令下，LLM不会等待用户决策，而是会自行静默仲裁，且仲裁结果常存在系统性偏向，prompt表述方式仅会改变仲裁的可见形式，难以消除隐性立场倾斜。
