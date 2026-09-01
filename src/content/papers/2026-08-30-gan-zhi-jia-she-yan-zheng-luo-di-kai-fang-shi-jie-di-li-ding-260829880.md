---
title: 'Perceive to Hypothesize, Verify to Ground: An Agentic Reasoning Framework
  for Open-World Geo-Localization'
title_zh: 感知假设-验证落地：开放世界地理定位的智能推理框架
authors:
- Yutian Jiang
- Ruijie Li
- Sisuo Lyu
- Xixuan Hao
- Qingxiang Liu
- Yongzi Yu
- Yuxuan Liang
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- The Hong Kong University of Science and Technology
arxiv_id: '2608.29880'
url: https://arxiv.org/abs/2608.29880
pdf_url: https://arxiv.org/pdf/2608.29880
published: '2026-08-30'
collected: '2026-09-01'
category: Agent
direction: Agent 多模态感知验证推理优化
tags:
- Agentic Reasoning
- Multimodal
- Geo-localization
- Tool Use
- Verification
one_liner: 提出双层感知-验证智能体框架GeoPAVE，缓解开放世界地理定位的感知幻觉与上下文漂移问题
practical_value: '- 可复用「单步生成多候选+不确定性标签引导工具调用」的架构，在电商多模态搜索、本地生活POI推荐场景中，先基于用户query/图像生成多个召回候选，为每个候选打不确定性标签（如语义匹配度低、属性缺失），针对性调用工具（如商品属性库检索、用户偏好查询、POI信息校验）验证，有效降低匹配幻觉，且推理成本远低于多rollout方案

  - 三类验证技能的设计可直接迁移：语言锚定（OCR/文本语义匹配）、场景验证（外部知识库检索）、上下文校验（关联信息交叉验证），适合电商商品图文匹配、虚假宣传识别、到店推荐场景验证等需求，规则化映射无需复杂RL训练，工程落地成本低

  - 可借鉴其分层评估思路，除最终准确率指标外，增加初始候选集覆盖率、错误修正率等中间指标，可快速定位推荐/搜索链路的瓶颈（如召回不足还是排序校验不足），优化迭代效率更高'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
开放世界地理定位需融合细粒度视觉线索与地理、文化等跨领域外部知识，现有LVLM方案存在两大核心痛点：一是模糊视觉线索下易触发感知捷径，将局部特征映射到高频地理区域；二是无约束工具调用易引入无关上下文，导致推理漂移，并行多rollout方案虽能提升效果但推理成本大幅上涨。
### 方法关键点
- 架构层面：采用双层解耦设计，感知模块单步推理生成最多3个结构化候选，每个候选包含坐标、置信度、推理依据、不确定性标签、推荐验证动作，同时基于不确定性做置信度校准抑制过度自信；
- 验证流程：基于不确定性标签规则化映射到三类验证技能，无需RL训练：语言锚定（OCR提取文字做地理约束）、场景验证（搜索引擎检索场景元数据）、上下文校验（POI/地形等地图信息做空间一致性校验），每个技能返回支持/反驳/修正决策，更新候选置信度，矛盾证据可直接否决候选；
- 数据集：构建PAVED数据集，从Foursquare真实用户签到数据筛选2524张可定位街景图像，配套完整的工具调用、假设验证推理轨迹，支持可解释Agent推理评测。
### 关键结果
在PAVED、MAPBench-V2、IM2GPS3K三个公开基准测试：以Gemini-3.0-Flash为底座时，相比底座模型，500m精度提升1.95pp，2km精度提升3.55pp，25km精度提升5.22pp，750km精度提升7.06pp，全面优于现有单步、多rollout的LVLM基线；以更弱的GPT-4o-mini为底座时，仍能稳定提升各阈值精度，750km精度提升达9.35pp，架构收益不依赖强底座能力。

最值得记住的结论：对于多模态模糊推理场景，「先广覆盖生成候选、再用可解释外部证据针对性验证」的架构，比单步推理或无约束多轮推理的性价比更高，且适配不同能力的底座模型。
