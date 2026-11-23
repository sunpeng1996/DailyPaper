---
title: 'Double counting in LLM evidence fusion: exact posteriors separate rule compliance
  from posterior gain'
title_zh: LLM证据融合的重复计数问题：用精确后验区分规则合规与收益
authors:
- Tengfei Shao
- Asma Rezaei
- Ali Reza Kamali
affiliations:
- Waseda University
- Anglia Ruskin University
- Cambridge Silicon Age Centre for Innovation
arxiv_id: '2611.27138'
url: https://arxiv.org/abs/2611.27138
pdf_url: https://arxiv.org/pdf/2611.27138
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: LLM 证据融合与去重优化
tags:
- LargeLanguageModel
- EvidenceFusion
- DoubleCounting
- BayesianInference
- PromptEngineering
one_liner: 提出分级依赖精确参考与配对收益协议，量化LLM证据去重指令的实际效果
practical_value: '- RAG/Agent记忆模块做证据去重时，不能仅验证规则合规度，要基于业务标注数据计算原始prompt与去重prompt的Brier分差值，避免强能力LLM因去重指令丢失有效信息

  - 可复用配对收益协议做小流量AB测：同一批请求同时跑原始和去重分支，对比和业务真值的误差差，成本低无需改动模型，可直接用于上线前验证

  - 多Agent共识、用户评论/多源商品信息聚合场景，可根据信息依赖度（完全复制/部分同源/独立来源）动态调整融合权重，比一刀切的「每源仅计一次」效果更优'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
RAG、多Agent共识、Agent记忆等场景中，LLM常将同源多份报告判定为独立证据导致重复计数，现有通用解决方案是添加「每源仅计一次」的prompt指令，但指令的实际价值高度依赖LLM原生融合能力，缺乏统一的量化基准，无法判断加指令后是增益还是损失。
### 方法关键点
- 构建分级依赖精确参考：固定单报告准确率0.65，设置4级同源依赖度δ（0=完全独立、0.3/0.6=部分依赖、1=完全复制），生成2976个二元判定世界，每个世界预设精确贝叶斯后验作为真值
- 设计配对收益协议：同一LLM分别在原始展示、同源信息分组、加去重指令、加依赖提示4种条件下回答，计算不同条件下回答与精确后验的均方误差差，明确区分规则合规度（与去重规则输出的匹配度）和实际收益（与真值的误差变化）
- 测试覆盖4个闭源LLM、2个开源LLM，所有测试成本仅99.45美元
### 关键结果
- δ=0时，claude-opus-5-5、gpt-6.1-sol对去重指令的合规率达100%，但与精确后验的误差反而上升0.044；gpt-6-luna合规率仅22%，误差下降0.014
- claude-haiku-5-5的收益随δ反转：δ=0时误差上升0.0295，δ=1时误差下降0.0302
- 去重指令的平均端到端收益差（δ=1减δ=0）为0.0342，95%置信区间[0.0303, 0.0382]
### 核心结论
LLM证据去重指令的价值完全取决于接收模型的原生基线能力，高合规不代表高收益，低合规也可能有正收益，必须基于业务场景实际测试后再决定是否上线
