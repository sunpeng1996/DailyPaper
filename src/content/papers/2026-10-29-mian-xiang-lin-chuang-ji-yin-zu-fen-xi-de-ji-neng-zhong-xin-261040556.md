---
title: Advancing Clinical Genomic Analysis with a Skill-Centred Agent
title_zh: 面向临床基因组分析的技能中心型大语言模型Agent
authors:
- Qiaoyu Zheng
- Weike Zhao
- Yanjie Fan
- Ye Cao
- Mengqi Jiang
- Xiao Zhou
- Xiaoman Zhang
- Pengcheng Qiu
- Yongguo Yu
- Yanfeng Wang
affiliations:
- Shanghai Jiao Tong University
- Shanghai AI Laboratory
- Xinhua Hospital affiliated to SJTU School of Medicine
- The Chinese University of Hong Kong
- Shanghai Chest Hospital
arxiv_id: '2610.40556'
url: https://arxiv.org/abs/2610.40556
pdf_url: https://arxiv.org/pdf/2610.40556
published: '2026-10-29'
collected: '2026-10-31'
category: Agent
direction: 垂直领域Agent · 技能编排落地
tags:
- LLM Agent
- Skill Orchestration
- Domain Specialization
- Human-AI Collaboration
- Tool Use
one_liner: 构建含105个临床基因组领域可执行技能的Agent，大幅提升分析准确率与人工协作效率
practical_value: '- 垂直领域Agent可复用「领域技能库+依赖感知编排+渐进式技能披露」架构，解决通用大模型hallucination与领域流程合规问题，电商/广告场景可将审核规则、品类计算逻辑、合规要求封装为原子技能，提升生成结果合规性

  - 人-AI协作效果评估可借鉴三条件平衡对照设计，对比无AI、通用LLM辅助、自研Agent辅助的业务效果，量化自研Agent的实际业务价值，可直接复用在电商客服、运营辅助等场景的效果验证

  - 垂直领域技能库建设可参考「LLM预筛选+领域专家人工校验+依赖关系建图」的流程，降低技能库的建设成本，电商场景可用来批量构建商品属性计算、优惠规则计算等标准化技能'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
临床基因组分析需要整合动态更新的指南、数据库、计算证据，测序普及后人工分析的高成本、高门槛成为临床转化的核心瓶颈，现有通用LLM/生物医疗Agent存在流程不符合领域规范、证据 hallucination 等问题，无法满足临床需求。

### 方法关键点
- 构建105个经过专家校验的原子可执行技能，分为指南类、检索类、分析类3种功能，覆盖基因组分析的全流程操作
- 设计技能图谱关联技能的语义相似性与硬依赖关系，推理时先根据用户请求召回初始技能，再扩展关联技能与前置依赖，渐进式披露技能指令降低上下文冗余
- 支持多模态输入（文本、家系图、临床文档、测序数据），执行过程留存全链路操作记录保障可解释性

### 关键结果数字
- 223例时间分隔基准测试集上，ClinGeX任务级宏平均准确率达71.7%，比最优基线高26个百分点，74.9%的报告可直接被临床医生采纳
- 45名临床专家参与的三条件对照试验中，ClinGeX辅助下3类场景的案例级准确率分别达51.1%、57.8%、64.4%，相比无AI辅助提升107%~128%，相比通用DeepSeek辅助提升222%~227%，单案例分析耗时最高缩短75%
- 1个月真实世界试点中，94.8%的任务结论被专家全部/部分采纳，77.3%的复杂任务节省15分钟以上时间

### 核心结论
垂直领域Agent的核心价值不是替代专家，而是通过标准化的可执行技能封装，降低领域操作门槛、提升专家工作效率，同时保障结果符合领域规范。
