---
title: 'MVWeaver: A Hierarchical Music Video Generation Agent with a Learned Song-to-Visual
  Bridge'
title_zh: MVWeaver：带习得歌视桥接模块的分层音乐视频生成Agent
authors:
- Sifei Li
- Minyan Luo
- Xu Li
- Guodong Qi
- Xincan Wang
- Hanwen Wang
- Chen Zhang
- Pengfei Wan
- Oliver Deussen
- Weiming Dong
affiliations:
- Institute of Automation, Chinese Academy of Sciences
- KlingAI Research
- University of Chinese Academy of Sciences
- Shanghai Theatre Academy
- Beijing Film Academy
arxiv_id: '2609.06478'
url: https://arxiv.org/abs/2609.06478
pdf_url: https://arxiv.org/pdf/2609.06478
published: '2026-09-06'
collected: '2026-09-10'
category: Agent
direction: 多模态生成Agent · 分层规划与模态桥接
tags:
- Agent
- Multimodal Generation
- LoRA
- Hierarchical Planning
- SFT
one_liner: 结合分层规划与LoRA微调习得的歌视桥接模块，提升MV生成的长时序连贯性与歌视匹配度
practical_value: '- 跨模态生成类Agent可复用「模态特征分析→领域桥接模块→分层规划→下游生成」的架构，解决模态匹配与长序列连贯性问题，可直接迁移到电商商品短视频自动生成场景

  - 垂域Agent缺乏领域知识时，可构造带rationale标注的真实配对数据集，用LoRA SFT轻量注入领域先验，大幅降低大模型微调成本，适配电商文案、营销素材生成等垂类需求

  - 长序列生成任务可引入分层规划机制，先做高层语义规划再落地细粒度执行，有效提升生成内容的全局一致性，适用于长图文种草、直播脚本生成等业务场景'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有自动MV生成系统仅能产出视觉合理的单镜头，普遍存在长时序连贯性差、视觉内容与歌曲语义匹配度低的问题，通用LLM缺乏歌视映射的垂直领域知识，难以直接输出符合行业规则的MV制作方案。
### 方法关键点
提出分层MV生成Agent MVWeaver，架构包含歌曲全维度分析、分层视觉规划、下游音视频生成渲染三大模块；构造1861组真实歌曲-MV配对数据集，标注歌曲侧、MV侧特征与歌视映射逻辑rationale，基于该数据集对通用LLM做LoRA SFT，习得歌曲分析到视觉规划的桥接能力，指导分层规划输出可执行的镜头方案。
### 关键结果
实验显示方案的歌视语义匹配度、视觉内容丰富度、全局概念连贯性、镜头间衔接流畅度均优于基线方案，消融实验验证了习得桥接模块的显著增益作用。
