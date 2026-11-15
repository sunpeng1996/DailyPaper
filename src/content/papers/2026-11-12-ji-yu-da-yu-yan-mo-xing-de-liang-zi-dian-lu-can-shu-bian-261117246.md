---
title: Programming Quantum Circuit Parameters with Large Language Models
title_zh: 基于大语言模型的量子电路参数编程
authors:
- Tiago de Souza Farias
- Caio Moraes Porto
- Matheus da Silva Fonseca
- Nicolas Armando Cabrera Carpi
- Anderson de Araujo Oliveira
- Celso Jorge Villas-Boas
affiliations:
- University of Innsbruck
- Federal University of São Carlos
arxiv_id: '2611.17246'
url: https://arxiv.org/abs/2611.17246
pdf_url: https://arxiv.org/pdf/2611.17246
published: '2026-11-12'
collected: '2026-11-15'
category: Other
direction: LLM量子电路参数生成研究
tags:
- LLM
- Quantum Computing
- Variational Quantum Circuit
- Parameter Optimization
one_liner: 探究通用LLM生成变分量子电路参数的适用边界与性能表现
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有研究表明LLM可跳过传统优化流程直接生成变分量子电路参数，但该方案的有效适用边界与约束条件尚未明确。
### 方法关键点
采用冻结的通用LLM，输入符号化电路与哈密顿量描述，支持可选的迭代能量反馈机制，在三类场景完成测试：通用随机哈密顿量、结构化母哈密顿量、分子系统。
### 关键结果
- 通用随机哈密顿量场景：LLM生成参数的能量误差高于传统Adam优化，额外迭代反馈带来的性能提升十分有限
- 结构化哈密顿量场景：LLM可生成具备竞争力的低能参数配置，可识别的物理/数学结构可显著降低参数推断难度
- LLM直接预测最小能量易违反哈密顿量谱下界，生成电路参数的方案可支持物理可实现能量期望值的独立校验
- LLM即使无法识别底层量子算法，仍可完成测量结果预测任务
