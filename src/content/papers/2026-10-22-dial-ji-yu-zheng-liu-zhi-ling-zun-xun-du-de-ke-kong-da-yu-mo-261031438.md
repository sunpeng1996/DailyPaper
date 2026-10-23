---
title: 'DIAL: Steerable Language Models with Distilled Instruction-Adherence Levels'
title_zh: DIAL：基于蒸馏指令遵循度的可控大语言模型
authors:
- Thanh Q. Tran
- John Russell Himawan
- Arun Verma
- Kiwan Wong
- Wei Xiao
- Daniela Rus
- Bryan Kian Hsiang Low
affiliations:
- National University of Singapore
- Singapore-MIT Alliance for Research and Technology
- MIT CSAIL
- Nanyang Technological University
arxiv_id: '2610.31438'
url: https://arxiv.org/abs/2610.31438
pdf_url: https://arxiv.org/pdf/2610.31438
published: '2026-10-22'
collected: '2026-10-23'
category: LLM
direction: LLM可控生成 · 指令遵循度控制
tags:
- Steerable LLM
- CFG Distillation
- Activation Steering
- Instruction Following
- Lightweight Adapter
one_liner: 通过蒸馏CFG多粒度指令遵循信号，实现轻量可扩展的LLM指令遵循度细粒度控制
practical_value: '- 电商营销/客服文案生成场景，可复用DIAL的细粒度控制逻辑，针对「风格活泼」「话术简洁」「突出优惠」等指令设置多档遵循度，匹配不同用户画像偏好，无需反复调整prompt，大幅提升生成效率

  - 推荐系统Agent的应答/工具调用场景，可复用轻量steering adapter架构，仅训练20M左右参数即可实现多指令的细粒度可控，无需微调全量LLM，也不需要为每条指令单独适配，96%+的吞吐量保留率适配线上低延迟要求

  - LLM生成内容的合规管控场景，可参考其CFG蒸馏的无标注训练范式，仅需合规指令文本即可训练适配器，不用人工标注响应，大幅降低合规控制模块的训练成本，还可灵活调整合规严格程度适配不同用户群体'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM的指令遵循度无法细粒度控制，用户或应用调整风格、合规、人设等要求时，需要反复修改prompt试错，效率极低。CFG类引导推理方法需要两次前向传播，推理成本翻倍；传统激活steering方法需要针对单条指令单独拟合，无法泛化到新指令，且缺乏中间遵循度的监督信号，调高控制强度易出现生成退化，无法同时满足细粒度控制、低推理成本、跨指令可扩展三个落地核心要求，在个性化生成、合规管控、用户自定义风格等场景落地受限。

### 方法关键点
- 以CFG生成的不同遵循度α下的token分布作为教师信号，蒸馏到轻量steering适配器，训练无需标注响应，仅需请求+指令文本即可完成
- 适配器仅20.6M参数，基于LLM隐藏层状态的文本条件分类器实现闭形式steering编辑，自适应根据目标α调整每token的steering强度，同时保留隐藏状态几何特征，避免生成内容不连贯
- 支持训练未见过的新指令泛化，无需单指令单独拟合，推理时仅需一次前向传播，原生适配vLLM等主流推理框架

### 关键结果
- 构造包含98625条指令的SteerIF数据集，覆盖概念、人设、可验证指令三类场景
- 在6个主流LLM家族（参数量1.2B~14B）上验证，概念、人设表达得分随α单调递增，可覆盖低于和高于常规prompt效果的遵循度区间
- vLLM部署下吞吐量保留基础LLM的96~99%，单token推理延迟与基础LLM几乎持平；训练GPU耗时仅为同类文本条件steering方法的1/4.65，可训练参数少12.4倍
- 结合常规prompt使用时，可验证指令遵循准确率比纯prompt最高提升4.1个百分点

### 核心结论
细粒度可控LLM的落地核心是平衡控制精度、推理效率、泛化能力，通过蒸馏LLM原生CFG的无标注信号可以用极低成本实现三者的最优权衡
